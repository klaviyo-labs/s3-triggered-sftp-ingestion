import boto3
import os

# arn:aws:iam::081586753487:user/nina


session = boto3.Session(
    aws_access_key_id=os.environ['ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['SECRET_ACCESS_KEY']

)

s3 = session.resource('s3')

# define the bucket name
bucket_name = os.environ['S3_BUCKET_NAME']
# the name you want to give to the file in S3
s3_file_name = os.environ['S3_FILE_NAME']
local_file = os.environ['LOCAL_FILE_NAME']

s3.meta.client.upload_file(Filename=local_file, Bucket=bucket_name, Key=s3_file_name)
