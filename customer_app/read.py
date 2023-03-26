import simplejson as json
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('CUSTOMERS_TABLE'))

def lambda_handler(event, context):
    # read id in the table passed as the path parameter in the event
    # patha parame is the id of the customer api/read/{id}
    id = int(event['pathParameters']['id'])
    # query the id from the table
    response = table.query( KeyConditionExpression=Key('id').eq(id))
    # return the response as json
    return {
        "statusCode": 200,
        "body": json.dumps(response['Items'])
    }