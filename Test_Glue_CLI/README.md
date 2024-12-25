aws s3 cp C:/Users/Strata/Desktop/my-data-assets/Test_Glue_CLI/test_cli_glue.py s3://data-assets-cli-test/scripts/

aws glue create-job \
  --name glue-cli-test \
  --role arn:aws:iam::058472766567:role/Gluepermisos \
  --command Name=glueetl,ScriptLocation=s3://data-assets-cli-test/scripts/test_cli_glue.py


aws glue update-job \
  --job-name MyJob \
  --job-update JobName=MyJob,Role=arn:aws:iam::058472766567:role/Gluepermisos,Command={Name=glueetl,ScriptLocation=s3://data-assets-cli-test/scripts/test_cli_glue.py}
