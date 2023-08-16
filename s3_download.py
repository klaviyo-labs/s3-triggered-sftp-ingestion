import boto3


def download_file_from_s3(aws_access_key_id, aws_secret_access_key, bucket_name, s3_file_name, downloaded_file):
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    s3 = session.resource('s3')
    
    s3.meta.client.download_file(Bucket=bucket_name, Key=s3_file_name, Filename=downloaded_file)



