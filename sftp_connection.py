import pysftp
import os


# ingest S3 file via SFTP
def connect_to_sftp_and_import_final_csv(final_file):
    with pysftp.Connection(host=os.environ['HOST'],
                           username=os.environ['USERNAME'],
                           private_key=os.environ['PRIVATE_KEY_PATH']) as sftp:
        print(f"Connected to {os.environ['HOST']}!")
        try:
            sftp.put(final_file, os.environ['PROFILES_PATH'])
            print(f"Imported {final_file}. Check your inbox for SFTP job details.")

        except Exception as err:
            raise Exception(err)

        # close connection
        pysftp.Connection.close(self=sftp)
        print(f"Connection to {os.environ['HOST']} has been closed.")
