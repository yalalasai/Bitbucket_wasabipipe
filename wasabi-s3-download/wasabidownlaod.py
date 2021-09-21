#import json


#data=open(r"D:\Office\AutomationTest Integration","w+")
#print(data)
import re
import sys
print(sys.path)
sys.path.append(r'C:\Users\Y Sai Krishna\AppData\Local\Programs\Python\Python37\Lib\site-packages')

import boto3

import os
Agilemanager_collector = {
        'AGM_SERVER': os.getenv("AGM_SERVER", "world"),
        'client_id': os.getenv("CLIENT_ID", "world"),
        'client_secret': os.getenv("CLIENT_SECRET", "world"),
        'db_host': os.getenv("DB_HOST","db"),
        'db_port': 27017
        }

s3client = boto3.client('s3',
                   endpoint_url='https://s3.us-central-1.wasabisys.com',
                   aws_access_key_id="389KPBIFHTMFVOBR957I",
                   aws_secret_access_key="gs4ibNWGNdXGOJuNCoUzCkIqzZoYsSAuHjmNr7D5")

s3 = boto3.resource('s3',
                   endpoint_url='https://s3.us-central-1.wasabisys.com',
                   aws_access_key_id="389KPBIFHTMFVOBR957I",
                   aws_secret_access_key="gs4ibNWGNdXGOJuNCoUzCkIqzZoYsSAuHjmNr7D5")


bucket_name = 'falkonsms-develop'
files=[]
bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    files.append(obj.key.rsplit('/')[-1])

string = ''.join(files)
match = re.findall(r"Falkon SMS Setup .*exe", string)
data=match[0].split("exe")


key_name = 'FalkonSMS/' + data[len(data)-2] + 'exe'
#print(key_name)
filename = data[len(data)-2] + "exe"
#print(filename)
s3client.download_file(Bucket=bucket_name,Filename=filename,Key=key_name)
