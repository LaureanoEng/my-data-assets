import boto3
import time

def run_athena_query_from_file(file_path, database, output_bucket):
    with open(file_path, 'r') as file:
        query = file.read()

    client = boto3.client('athena')

    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
        },
        ResultConfiguration={
            'OutputLocation': output_bucket
        }
    )

    query_execution_id = response['QueryExecutionId']

    # Espera a que la consulta se complete
    status = 'RUNNING'
    while status == 'RUNNING':
        response = client.get_query_execution(QueryExecutionId=query_execution_id)
        status = response['QueryExecution']['Status']['State']
        if status in ['FAILED', 'CANCELLED']:
            raise Exception('Athena query failed or was cancelled')
        time.sleep(5)

    # Obtén los resultados de la consulta
    result_response = client.get_query_results(QueryExecutionId=query_execution_id)
    return result_response

# Uso de la función
file_path = 'C:/Users/Strata/Desktop/my-data-assets/Run_Athena_Query/sql_query/test.sql'
database = 'analytics_dev'
output_bucket = 's3://athena-queries-strata-analytics/'

results = run_athena_query_from_file(file_path, database, output_bucket)
print(results['ResponseMetadata'])