import pandas as pd
import os


# anticipate column mapping based on commonly used headers
def suggest_column_mapping(loaded_file):
    column_mapping = {
        'Email': ['EmailAddress', 'person.email', 'Email', 'email', 'emailaddress', 'email address',
                  'Email Address', 'Emails'],
        'PhoneNumber': ['Phone#', 'person.number', 'phone', 'numbers', 'phone number', 'Phone Number']
    }

    suggested_mapping = {}
    for required_header, old_columns in column_mapping.items():
        for column in old_columns:
            if column in loaded_file.columns:
                suggested_mapping[column] = required_header

    return suggested_mapping


# map column headers of S3 file & add List ID column
def map_column_headers(loaded_file, list_id):
    mapped_file = loaded_file.rename(columns=suggest_column_mapping(loaded_file), inplace=False)
    mapped_file['List ID'] = list_id

    final_file = os.environ['FOLDER_PATH'] + os.environ['MAPPED_FILE_NAME']
    mapped_file.to_csv(final_file, index=False)

    return final_file
