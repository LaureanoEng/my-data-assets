
import boto3
import time
import pandas as pd

def run_athena_query_and_save_to_csv(file_path, database, output_bucket, csv_output_path):
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

    # Procesa los resultados y guárdalos en un CSV
    rows = result_response['ResultSet']['Rows']
    headers = [col['VarCharValue'] for col in rows[0]['Data']]
    data = []

    for row in rows[1:]:
        data.append([col.get('VarCharValue', None) for col in row['Data']])

    df = pd.DataFrame(data, columns=headers)
    df.to_csv(csv_output_path, index=False)

    print(f'Results saved to {csv_output_path}')

# Uso de la función
file_path = './sql_query/test.sql'
database = 'prod-iguana-amdocs'
output_bucket = 's3://aws-athena-query-results-us-east-1-509654266774//'
csv_output_path = './sql_query/results/output.csv'

run_athena_query_and_save_to_csv(file_path, database, output_bucket, csv_output_path)