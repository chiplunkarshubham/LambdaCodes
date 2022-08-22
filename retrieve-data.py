'''
arn:aws:execute-api:us-east-1:836106600136:5mto7ucjqa/*/GET/operations
API endpoint: https://5mto7ucjqa.execute-api.us-east-1.amazonaws.com/Dev/operations
Details
API type: REST
Authorization: NONE
Method: GET
Resource path: /operations
Service principal: apigateway.amazonaws.com
Stage: Dev
Statement ID: 3a662e68-2ef9-41a9-8c28-b5a046a34cad
lambda function name: retrieve-data
'''


'''
Python program to retrieve data from DynamoDb with exception handling taken care of.
Exception should be raised when: 
    1) If the passed Emp_Id does not exist in the table.
    2) If anything apart from Emp_Id is passed, it should prompt that only Emp_Id should be supplied nothing else.
Code By Shubham Chiplunkar
'''

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Emp_Master')

def lambda_handler(event, context):
    try:
        id = event['Emp_Id']
        get_data = table.get_item(Key={'Emp_Id': id})
        return {
            'statusCode': 200,
            'details': get_data['Item']
        }
    except:
        try:
            return {
               'message' : "Employee with id as "+str(id)+" does not exist" ,
            }
        except UnboundLocalError:
            return{
                'message' : "Only Employee id in the format Emp_Id should be provided to get the details"
            }