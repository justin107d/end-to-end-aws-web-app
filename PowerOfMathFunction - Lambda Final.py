import json
import math
from time import gmtime, strftime

# import the AWS SDK (for Python the package name is boto3)
import boto3

# create a DynamoDB object using the AWS SDK
# use the DynamoDB object to select our table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PowerOfMathDatabase')

now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

    # extract the two numbers from the Lambda service's event object
    mathResult = math.pow(int(event['base']), int(event['exponent']))

    # write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': str(mathResult),
            'LatestGreetingTime':now
            })

    # return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': json.dumps('Your result is ' + str(mathResult))
    }