import sys
import os

import boto3

try:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    S3_REGION_NAME = os.environ['S3_REGION_NAME']
    S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
except KeyError as e:
    print(f"ERROR: Key {e} is not defined")

s3 = boto3.resource('s3',
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name=S3_REGION_NAME)

def main():
    try:
        if sys.argv[1] is not None:
            try:
                f = open(sys.argv[1],'rb')
            except FileNotFoundError as e:
                f = None
                print("Upload error: File Not Found")
        else:
            print("Upload error: You must specify a file to upload")
        if len(sys.argv) == 3 and f is not None:
            try:
                if sys.argv[2].endswith("/"):
                    path = f"{sys.argv[2]}{sys.argv[1]}"
                else:
                    path = f"{sys.argv[2]}/{sys.argv[1]}"
                s3.Bucket(S3_BUCKET_NAME).upload_fileobj(f,path)
                print(f"File uploaded to {path}")
            except Exception as e:
                print(f"Error while Uploading: {e}")
        elif len(sys.argv) == 2 and f is not None:
            try:
                s3.Bucket(S3_BUCKET_NAME).upload_fileobj(f,sys.argv[1])
                print(f"File uploaded to {sys.argv[1]}")
            except Exception as e:
                print(f"Error while Uploading: {e}")
        else:
            pass
    except Exception as e:
        print(f"Error: {e}. You must specify a file and path to upload to.")

if __name__ == '__main__':
    main()
