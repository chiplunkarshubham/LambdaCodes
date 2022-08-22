'''
Bucket arn: arn:aws:s3:::shubhamchiplunkar-source
Event type: s3:ObjectCreated:*
lambda function name: lambda-for-addition
'''

'''
Python program to sync objects when uploaded from the source bucket to destination buckets.
Code by Shubham Chiplunkar
'''

import boto3

s3_client=boto3.client('s3')

def repeat(s,d,f):
    copy_object={'Bucket':s,'Key':f}
    s3_client.copy_object(CopySource=copy_object,Bucket=d,Key=f) # Copying File from source to destination
    
def lambda_handler(event, context):
    source=event['Records'][0]['s3']['bucket']['name'] # Source Bucket
    file=event['Records'][0]['s3']['object']['key'] # Name of the file that has been uploaded
    d1='shubhamchiplunkar-destination1' # Name of Destination Bucket 1
    d2='shubhamchiplunkar-destination2' # Name of Destination Bucket 2
    repeat(source, d1,file) 
    repeat(source, d2,file)
