
import csv,json
from io import StringIO
import boto3
import os



#Getting Access Key and Secret Access Key from CSV file
#Opening the security file
with open("Md.Osman-Nayeem_accessKeys.csv") as key:
    #Storing the contents of security file in the created variable aws_key
    aws_key = key.read()
    aws_key = StringIO(aws_key)
# convert csv to json
fieldnames = ("access_key", "secret_access_key")
#Reading the CSV values
csv_reader = csv.DictReader(aws_key, fieldnames)
#print(csv_reader)
#Converting into Json
json_data = json.dumps([row for row in csv_reader])
aws_key_json = json.loads(json_data)
#print(aws_key_json)
#Storing the access key and secret key into variables
access_key= str(aws_key_json[1]["access_key"])
secret_access_key=  str(aws_key_json[1]["secret_access_key"])
#print(type(access_key))
bucket_name = 'midtermgroupthree'