import boto3
import botocore
from decouple import config
s3 = boto3.resource('s3',aws_access_key_id=config("aws_access_key"),
            aws_secret_access_key=config("aws_secret_key"),)
def downloadfiles(BUCKET_NAME):
    try:
        my_bucket = s3.Bucket(BUCKET_NAME)
        for file in my_bucket.objects.all():
            s3.Bucket(BUCKET_NAME).download_file(file.key, f"./samples/{file.key}_copy")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            print("Bucket doesn't exist")
downloadfiles("bucketname")