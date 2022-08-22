'''
API endpoint: https://5mto7ucjqa.execute-api.us-east-1.amazonaws.com/Dev/operations
Details
API type: REST
Authorization: NONE
Method: POST
Resource path: /operations
Service principal: apigateway.amazonaws.com
Stage: Dev
Statement ID: 76b54e42-792b-48a6-b6f8-21fea8725050
lambda function name: store-data
'''

'''
Python program to store the data into DynamoDB
Code by Shubham Chiplunkar
'''

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Emp_Master')

def lambda_handler(event, context):
    table.put_item(Item=event)
    return {
        'statusCode': 200,
        'message': "Employee details have been inserted successfully"
    }


