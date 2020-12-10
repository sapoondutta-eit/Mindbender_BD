import boto3
import botocore
from boto3.s3.transfer import S3Transfer

BUCKET_NAME = 'enhance-it' # replace with your bucket name
KEY = 'nissan.jpg' # replace with your object key

# s3 = boto3.client('s3')
# # obj = s3.Object(BUCKET_NAME,KEY)
# # new_obj = obj.get()['Body'].read()
# # print(new_obj)
# # s3.Bucket(BUCKET_NAME).download_file(Key=KEY, Filename='froms3.jpg')
# # #s3.upload_fileobj(f, "us-east-1-tip-s3-stage", "folder1/folder2/test_audit_log.txt")

# # response = s3.put_object(Bucket=BUCKET_NAME, Key='lituation/' # note the ending "/"

# # s3.Bucket(BUCKET_NAME).upload_file("/home/marcus/Downloads/nissan.jpg", "lituation/picture.jpg")

# #s3.meta.client.upload_file(Filename='/home/marcus/Downloads/nissan.jpg', Bucket=BUCKET_NAME, Key='s3_output_key')

# transfer = S3Transfer(s3)
# transfer.upload_file('/home/marcus/Downloads/nissan.jpg', BUCKET_NAME, 'lituation'+"/"+'nissan.jpg')


s3 = boto3.resource(service_name = 's3')
s3.meta.client.upload_file(Filename = '../../Downloads/nissan.jpg', Bucket = BUCKET_NAME, Key ='lituation'+"/"+'nissan2222.jpg')

