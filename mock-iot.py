import datetime
import json
import random
import boto3

STREAM_NAME = "reaqtions-iot-data-stream"

def get_iot_data():
    return {
            'TIME': datetime.datetime.now().isoformat(),
            'USER_INPUT': random.choice([1,2,3,4,5]),
            'NO2': random.choice([1,2,3,4,5]),
            'CO': random.choice([1,2,3,4,5]),
            'PM01': random.choice([1,2,3,4,5]),
            'PM2_5': random.choice([1,2,3,4,5]),
            'PM10': random.choice([1,2,3,4,5]),
            'AQI': random.choice([1,2,3,4,5]),
            'eCO2': round(random.random() * 1000, 2),
            'TVOC': random.choice([1,2,3,4,5]),
            'P': round(random.random() * 100, 2),
            'T': round(random.random() * 100, 2),
            'RH': round(random.random() * 100, 2)
    }

def generate(stream_name, kinesis_client):
    count = 0
    while True:
        count+=1
        response = kinesis_client.put_record(
           DeliveryStreamName=stream_name,
           Record={
                'Data': json.dumps(get_iot_data())
            }
        )
        record_id = response.get('RecordId')
        print(f"Record # {count} Sent to AWS Cloud | Record ID ", str(record_id)[:5])


if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('firehose'))