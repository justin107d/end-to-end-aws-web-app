import json
import math

# Define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    
    # extract the numbers from the Lambda service's event object
    mathResult = math.pow(int(event['base']), int(event['exponent']))

    return {
        'statusCode': 200,
        'body': json.dumps('Your result is: ' + str(mathResult))
    }