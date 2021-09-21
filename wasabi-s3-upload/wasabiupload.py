#import json


#data=open(r"D:\Office\AutomationTest Integration","w+")
#print(data)
import re
import sys
print(sys.path)
sys.path.append(r'C:\Users\Y Sai Krishna\AppData\Local\Programs\Python\Python37\Lib\site-packages')

import boto3
from boto3.s3.transfer import TransferConfig


s3client = boto3.client('s3',
                   endpoint_url='https://s3.us-central-1.wasabisys.com',
                   aws_access_key_id="389KPBIFHTMFVOBR957I",
                   aws_secret_access_key="gs4ibNWGNdXGOJuNCoUzCkIqzZoYsSAuHjmNr7D5")

s3 = boto3.resource('s3',
                   endpoint_url='https://s3.us-central-1.wasabisys.com',
                   aws_access_key_id="389KPBIFHTMFVOBR957I",
                   aws_secret_access_key="gs4ibNWGNdXGOJuNCoUzCkIqzZoYsSAuHjmNr7D5")


# Set the desired multipart threshold value (5GB)
GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5*GB)


bucket_name = 'falkonsms-develop'
files=[]
bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    files.append(obj.key.rsplit('/')[-1])

string = ''.join(files)
match = re.findall(r"Falkon SMS Setup .*exe", string)
data=match[0].split("exe")


key_name = 'FalkonSMS/CICD_Pipeline_Test.exe'
#print(key_name)
file_path = "D:\Office\AutomationTest Integration\CICD_Pipeline_Test.exe"
filename = data[len(data)-2] + "exe"
#print(filename)
#s3client.download_file(Bucket=bucket_name,Filename=filename,Key=key_name)
s3client.upload_file(Bucket=bucket_name,Filename=file_path, Key=key_name)
