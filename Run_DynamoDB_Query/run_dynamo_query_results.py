import boto3
import csv
from datetime import datetime

# Configura tu cliente DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cwc-exit-duke-s3-in-metadata')

# Obtiene la fecha actual en formato YYYYMMDD
fecha_actual = datetime.now().strftime('%Y%m%d')

# Realiza el escaneo
response = table.scan(
    FilterExpression=boto3.dynamodb.conditions.Attr('creation_date').eq(fecha_actual)
)

# Procesa los resultados
items = response['Items']

if not items:
    print("No se encontraron resultados para la fecha actual.")

# Exporta a CSV
with open(f'./Run_DynamoDB_Query/{fecha_actual}_resultados.csv', 'w', newline='') as csvfile:
    if items:
        fieldnames = items[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in items:
            writer.writerow(item)
    else:
        print("No hay datos para escribir en el archivo CSV.")

print("Consulta completada y resultados exportados a resultados.csv")
