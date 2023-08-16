import configure_csv
import sftp_connection
import s3_download
import os
import pandas as pd
import json


def lambda_handler(event, context):
    s3_download.download_file_from_s3(os.environ['ACCESS_KEY_ID'], os.environ['SECRET_ACCESS_KEY'],
                                      os.environ['S3_BUCKET_NAME'], os.environ['S3_FILE_NAME'],
                                      os.environ['FOLDER_PATH'] + os.environ['LOCAL_FILE_NAME'])
    loaded_file = pd.read_csv(os.environ['FOLDER_PATH'] + os.environ['LOCAL_FILE_NAME'])
    final_file = configure_csv.map_column_headers(loaded_file, os.environ['LIST_ID'])
    sftp_connection.connect_to_sftp_and_import_final_csv(final_file)

    return {
        'statusCode': 200,
        'body': json.dumps('successfully ran lambda'),
    }

# uncomment for local testing \ comment for deployment to AWS
# lambda_handler(event='', context='')
