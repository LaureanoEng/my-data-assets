
# Data Asset - Despliegue & Actualización AWS Lambda con AWS CLI

Este documento proporciona los pasos necesarios para desplegar y actualizar una función AWS Lambda utilizando la CLI de AWS.
Este es solo un ejemplo simple, pero el CLI permite realizar múltiples configuraciones. 

### Para más información:
[AWS CLI - Lambda](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html)

[AWS CLI - Lambda - Create Function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html)

[AWS CLI - Lambda - Update Function Code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html)

[AWS CLI - Lambda - Update Function Configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html)


## Prerrequisitos

1. **AWS CLI instalada**: Asegúrate de tener instalada la AWS CLI. Si estás en Windows o Mac puedes descargar el instalador desde el siguiente link [AWS CLI Install](https://aws.amazon.com/es/cli/) o en Linux, puedes instalarla con el siguiente comando:

```sh
sudo snap install aws-cli --classic
```

2. **Lambda Role**: Para poder realizar el despliegue de la lambda uno de los parametros obligatorios es el rol que esta va a asumir con sus permisos. La creación del rol se puede realizar desde la consola de AWS y configurar los permisos necesarios.
En caso de querer realizarlo desde la consola está este link de interes: [AWS CLI - IAM - Create Role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html)


## Crear Estructura de Carpeta de Lambda
Podemos tener Lambdas más simples y más complejas. Antes de realizar el deploy, es importante tener todo lo que se necesita subir en una sola carpeta que es la que se va a zippear.

### Ejemplo de Estructura Simple de AWS Lambda

```text
my-simple-lambda-project/
├── lambda_function.py
├── requirements.txt
└── README.md
```

### Ejemplo de Estructura Compleja de AWS Lambda

```text
my-complex-lambda-project/
├── src/
│   ├── handlers/
│   │   └── lambda_function.py
│   └── utils/
│       └── helper.py
├── tests/
│   └── test_lambda_function.py
├── config/
│   └── settings.yaml
├── assets/
│   └── sample_data.json
├── build/
├── dist/
├── scripts/
│   └── deploy.sh
├── requirements.txt
└── README.md
```

## Despliegue
### Empaquetado de código
En Windows Powershell:
```powershell
Compress-Archive -Path "C:/path/to/my-lambda-project/lambda_function.py" -DestinationPath "C:/path/to/my-lambda-project/lambda_function.zip"
```

En Linux:
```sh
zip lambda_function.zip lambda_function.py
```

### Despliegue del código
Todos los parámetros utilizados en este ejemplo son **obligatorios** para el depliegue a excepción de `--publish` que nos permitirá llevar versiones de las lambdas en la misma función. Esto es clave porque nos permitirá volver a una versión anterior de manera muy rápida en caso de fallos sin necesidad de tener que realizar en debugging en tiempo real.

```sh
aws lambda create-function --function-name test-cli-lambda --runtime python3.10 --role arn:aws:iam::058472766567:role/test-cli-lambda --handler lambda_function.lambda_handler --zip-file fileb://CLI_Lambda/lambda_function.zip --publish
```

### Actualizar Función Lambda (Código)
```sh
aws lambda update-function-code --function-name test-cli-lambda --zip-file fileb://CLI_Lambda/lambda_function.zip --publish
```

### Actualizar Función Lambda (Configuración)
```sh
aws lambda update-function-configuration --function-name test-cli-lambda --memory-size 511
```
