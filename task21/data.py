import boto3
import botocore

BUCKET_NAME = 'enhance-it' # replace with your bucket name
KEY = 'nissan.jpg' # replace with your object key

s3 = boto3.resource('s3')
# obj = s3.Object(BUCKET_NAME,KEY)
# new_obj = obj.get()['Body'].read()
# print(new_obj)
s3.Bucket(BUCKET_NAME).download_file(Key=KEY, Filename='froms3.jpg')
