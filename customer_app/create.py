import boto3
import os
import json

# Create a dynamodb resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('CUSTOMERS_TABLE'))

# def a lambda function that will be called when the table is created
def lambda_handler(event, context):
    # put item in the table passed in the event parameter as json
    customer = json.loads(event['body'])
    table.put_item(Item=customer)
    return {
        "statusCode": 200,
        "body": json.dumps({ "message": "Customer created successfully" })
    }



    # Create a new item in the table
    # table.put_item(
    #     Item={
    #         'CUSTOMER_ID': '1234',
    #         'CUSTOMER_NAME': 'John Doe',
    #         'CUSTOMER_EMAIL': 'qwyeywqe@email.com'
    #     }
    # )