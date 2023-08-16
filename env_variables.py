# constants to be configured & added into AWS environment variables

# configured in AWS
ACCESS_KEY_ID = "swap in your AWS access key ID"
SECRET_ACCESS_KEY = "swap in your access key"
S3_BUCKET_NAME = "swap in your S3 bucket name"

# folder path to where you are saving your S3 file locally
FOLDER_PATH = "swap in folder path"

S3_FILE_NAME = "swap in S3 file name"

LOCAL_FILE_NAME = f"{S3_FILE_NAME}_local.csv"

MAPPED_FILE_NAME = "mapped_profiles.csv"

# replace with your 6 digit List ID found in the URL of the subscriber List.
LIST_ID = "ABC123"

PROFILES_PATH = "/profiles/profiles.csv"

# folder path to where your SSH private key is stored
PRIVATE_KEY_PATH = "swap in private key folder path"

HOST = "sftp.klaviyo.com"

# replace with your assigned username found in the UI of Klaviyo's SFTP import tool
USERNAME = "swap in username"
