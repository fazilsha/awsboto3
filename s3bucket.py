import boto3
from decouple import config
import os
class S3op():
    def __init__(self):
        self.service = boto3.client(
            's3',
            aws_access_key_id=config("aws_access_key"),
            aws_secret_access_key=config("aws_secret_key"),
        )
    def s3bucketcreate(self,Bucket):
        try:
            self.service.create_bucket(Bucket=Bucket)
            print("Bucket created sucessfully")
        except:
            print("Bucket already exist!")
    def s3BucketUpload(self,Bucket,files):
        for file in files:
            try:
                with open(f"{file}", "rb") as f:
                    self.service.upload_file(file,Bucket,file)
                    print(f'Filename: {file}')
            except:
                print(f"Filename: {file} doesn't exist")
B=S3op()
B.s3bucketcreate("mybucketname")
B.s3BucketUpload("mybucketname",["test1.txt","test2.txt"])
