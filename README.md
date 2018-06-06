# s3-uploader

### Simple Python script to upload to s3
First export appropriate environment variables:
```
export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
export S3_REGION_NAME=<REGION_YOUR_BUCKET_IS_IN>
export S3_BUCKET_NAME=<NAME_OF_YOUR_BUCKET>
```

The script has one required flag to run, the filename. This will upload the file to the root path of the bucket:
```
python upload.py file.txt
```

You can also specify the upload path like:
```
python upload.py file.txt data/test
# will upload to /data/test/file.txt in the bucket
```

### TODO
- Upload entire directory
