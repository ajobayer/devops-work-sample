import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image
from datetime import datetime

s3_client = boto3.client('s3')

def timestamp_pdf_file(image_path, git lo):
    print("image_path =", image_path)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        print('Buckername: {} '.format(bucket))
        key = unquote_plus(record['s3']['object']['key'])
        print('Buckername: {} '.format(key))
        tmpkey = key.replace('/', '')
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        upload_path = '/tmp/timestamp-{}'.format(tmpkey)
        s3_client.download_file(bucket, key, download_path)
        timestamp_pdf_file(download_path, upload_path)
        s3_client.upload_file(upload_path, '{}-timestamp'.format(bucket), key)
