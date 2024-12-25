# AWS Glue CLI - Ejemplo de Uso

Este documento proporciona ejemplos de comandos para copiar un script a un bucket de S3 y crear o actualizar un trabajo de AWS Glue utilizando la CLI de AWS.

## Prerrequisitos

1. **AWS CLI instalada**: Asegúrate de tener instalada la AWS CLI. Si estás en Windows o Mac puedes descargar el instalador desde el siguiente link [AWS CLI Install](https://aws.amazon.com/es/cli/) o en Linux, puedes instalarla con el siguiente comando:

```sh
sudo snap install aws-cli --classic
```


## Despliegue

### Copiar el Script a S3
Utiliza el siguiente comando para copiar el script test_cli_glue.py a un bucket de S3:

```sh
aws s3 cp C:/Users/Strata/Desktop/my-data-assets/Test_Glue_CLI/test_cli_glue.py s3://data-assets-cli-test/scripts/
```

### Crear un Trabajo de AWS Glue
Utiliza el siguiente comando para crear un trabajo de AWS Glue:

```sh
aws glue create-job \
  --name glue-cli-test \
  --role arn:aws:iam::058472766567:role/Gluepermisos \
  --command Name=glueetl,ScriptLocation=s3://data-assets-cli-test/scripts/test_cli_glue.py
```

### Actualizar un Trabajo de AWS Glue
Utiliza el siguiente comando para actualizar un trabajo de AWS Glue existente:

```sh
aws glue update-job \
  --job-name MyJob \
  --job-update JobName=MyJob,Role=arn:aws:iam::058472766567:role/Gluepermisos,Command={Name=glueetl,ScriptLocation=s3://data-assets-cli-test/scripts/test_cli_glue.py}
```

### Referencias
* [AWS CLI - Glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html)

* [AWS CLI - S3](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html)

