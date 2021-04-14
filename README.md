# awsboto3
Accessing AWS services using Python Boto3 client
#sample output for B.listBuckets()
=> refer s3bucket.py--> listBuckets
------------------------------------------------------------
Bucket Name: s3bucketsample1 | Created on: Mon Apr 12 17:25:55 2021
--------Files in bucket---------
test1.txt
test2.txt
------------------------------------------------------------
Bucket Name: s3bucketsample2 | Created on: Tue Mar  9 09:20:31 2021
--------Files in bucket---------
101.pdf
101.pdf
beginners_python_cheat_sheet_pcc_all.pdf
pdf_sample1.pdf
------------------------------------------------------------

#Downloading files
REFER: downloadS3files.py

downloadfiles("bucketname")
1. This function accepts a parameter for bucket name.
2. once we configured the access and secret key with required service.We all set to go!!
3. It will fetch all files from the bucket which we mentioned:
4. And download it in our desired location.
e.g I stored downloaded files in a samples directory ./samples/{file.key}_copy
