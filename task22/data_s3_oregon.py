import boto3
import botocore
from boto3.s3.transfer import S3Transfer


BUCKET_NAME = 'bucket-eit-sapoondutta001'

# client = boto3.client('s3', region_name='us-west-2')
s3 = boto3.resource(service_name = 's3',region_name='us-west-2')
s3.meta.client.upload_file(Filename = '../../Downloads/nissan.jpg', Bucket = BUCKET_NAME, Key ='lituation'+"/"+'nissan2222.jpg')
