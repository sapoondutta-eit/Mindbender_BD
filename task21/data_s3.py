bucket = 'enhance-it'
import boto3
import pydoop.hdfs as hdfs 

s3 = boto3.resource('s3')


file = hdfs.open('hdfs://master:9000/data_for_db/currency=USD/part-00000-f65c545f-baa0-4bf0-8aa9-0b14957848c4.c000.json')
s3.Bucket(bucket).put_object(Key='lituation/data_from_hdfs.csv', Body=file)