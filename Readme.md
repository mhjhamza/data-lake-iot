# ReAQtions
## _AWS Cloud Near Real-time Data Ingestion_

Architect, Develop and Deploy the AWS Infrastructure to support the near real-time ingestion of data from IoT Devices.
## Modules

- Ingestion
- Storage
- Transformation
- Logging
- Reporting

### Ingestion

Ingestion Module is responsible for ingesting the near real-time data into the AWS Cloud. THe data ingestion is performed with the [Amazon Kinesis Data Firehose](https://aws.amazon.com/kinesis/data-firehose/). Amazon Kinesis Data Firehose (`reaqtions-iot-data-stream`) allows you to reliably load real-time streams into data lakes, warehouses, and analytics services. Amazon Kinesis Data Firehose is an extract, transform, and load (ETL) service that reliably captures, transforms, and delivers streaming data to data lakes, data stores, and analytics services. The services are chosen considering the robustness and scalability in mind. 

![](https://d1.awsstatic.com/pdp-how-it-works-assets/product-page-diagram_Amazon-KDF_HIW-V2-Updated-Diagram@2x.6e531854393eabf782f5a6d6d3b63f2e74de0db4.png)

### Storage

Storage is responsible for storing the data in an S3 bucket. Following the Data Lake arhitecture, any data that is ingested via the Kinesis Firehose will land in the S3 Bucket or RAW Zone (i.e. `reaqtions-iot-data-lake-raw`). The data will be stored within the bucket under the prefix (folder) named `processed`. The data files path looks like `reaqtions-iot-data-lake-raw/iot/{timestamp.csv}`.

Even though the solution is error proof, still if there comes a scenario where the data couldn't be handled properly or is malformed, It will be stored under the prefix `/error` instead of `/processed`.

![](https://d1.awsstatic.com/s3-pdp-redesign/product-page-diagram_Amazon-S3_HIW.cf4c2bd7aa02f1fe77be8aa120393993e08ac86d.png)

### Transformation
**reaqtions-data-transformation** Lambda Function which is a serverless compute is used for the transformations. The records ingestied by the Kinesis Firehose Stream and stored as multiline JSON objects if not transformed. This doesn't allow the reporting part to integrate. Hence, the records are first transformed into multiple JSON files and stored under `/processed` prefix.

### Logging
All the transformation logs are available under AWS' service CloudWatch. 
Check Log Group `/aws/lambda/reaqtions-data-transformation`.

### Reporting

Reporting module is responsible is connecting to the S3 Bucket based on the aws configurations (AWS). `aws_access_key_id` and `aws_secret_access_key`. Reporting module consists a Python script that fetching the data from AWS cloud and load that data into an array or pandas dataframe. This data can be linked with the existing script for reporting purposes.


### How to configure aws

- Go to IAM Console under your [IAM User](https://us-east-1.console.aws.amazon.com/iam/home#/users/nabram_admin?section=security_credentials) and get the credentials
- Click **Create access key**
- Install the [`AWS CLI`](https://aws.amazon.com/cli/)
- Run `$ aws configure`

```AWS Access Key ID [None]: AKIAIOSF******MPLE
AWS Secret Access Key [None]: wJal****XAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```
- Now run `python mock-iot.py` 
- Open the S3 bucket, refresh and verify the data.
- Stop the mock-iot script.
- Now run `python reporting.py` 

