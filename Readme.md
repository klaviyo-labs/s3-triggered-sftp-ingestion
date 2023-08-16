# S3 Filedrop-Triggered SFTP Ingestion

# Overview
Updating and importing a large number of profiles in Klaviyo can be a time-consuming process. While it's possible to ingest data using Klaviyo API [endpoints](https://developers.klaviyo.com/en/reference/update_profile), it can take approximately 7-8 hours to fully update ~250K profiles. To address this challenge, we present an AWS-based solution that leverages an S3 bucket and [Klaviyo's SFTP import tool](https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool_).


# Project Overview
The aim of this project is to streamline and accelerate the process of ingesting profile and event data into Klaviyo using AWS services and Klaviyo's SFTP import tool. The proposed solution involves setting up an S3 bucket and running a lambda function on an AWS instance. The function relies on an S3 file drop to trigger profile data ingestion to Klaviyo's SFTP server. The data stored in the S3 bucket can include key attributes such as birthdate, favorite brands and any other relevant properties that you would like to ingest into Klaviyo.

# Features
* Efficiently updates and imports profiles with relevant data to leverage in Klaviyo.
* Utilizes Klaviyo's SFTP import tool for seamless integration.
* Leverages AWS services, including S3 and lambda for speed and flexibility of use.
* Automates the update and import process, reducing manual effort and saving time.
* Improves data accuracy and reduces the risk of errors in ingestion.

# Getting Started
To configure this solution for updating and importing profiles in Klaviyo, follow these steps:

* Set up an AWS account and ensure you have access to S3, lambda, and [IAM](https://console.aws.amazon.com/iam/).
* Create an IAM execution role for Lambda with the following policy names:
  * AmazonS3FullAccess
  * AWSLambdaBasicExecutionRole
* Create access key from Security credentials tab and record corresponding ID and secret key.
* Create an [S3 bucket](https://console.aws.amazon.com/s3/).
* Create a [Lambda function](https://console.aws.amazon.com/lambda/) with the configured execution role.
  * Configure the trigger settings to the corresponding S3 bucket
* Configure environment variables with corresponding parameters. 
* Deploy the Lambda function and monitor progress to ensure profiles are updated and displayed in Klaviyo's UI as anticipated.

# License
This project is licensed under the MIT License. Feel free to use and modify it according to your needs.

# Please Note:
This README provides a high-level overview of the project and may require developer resources to implement.
