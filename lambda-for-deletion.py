'''
Bucket arn: arn:aws:s3:::shubhamchiplunkar-source
Event type: s3:ObjectRemoved:*
lambda function name: lambda-for-deletion
'''

'''
Python program to sync objects when deleted from the source bucket to destination buckets.
Code by Shubham Chiplunkar
'''

import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    s3.delete_object(Bucket="shubhamchiplunkar-destination1", Key=event['Records'][0]['s3']['object']['key']) # Code to delete the specified object in specified bucket
    s3.delete_object(Bucket="shubhamchiplunkar-destination2", Key=event['Records'][0]['s3']['object']['key']) # key is the name of the file that got deleted
    
    



    