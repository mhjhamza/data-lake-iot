import awswrangler as wr
bucket = 'reaqtions-iot-data-lake-raw'
prefix = 'processed'
data = wr.s3.read_json(f"s3://{bucket}/{prefix}/")
print('Total Records Found:', len(data))