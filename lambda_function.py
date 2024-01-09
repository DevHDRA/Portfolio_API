import json
from api import apiHandler

def lambda_handler(event, context):
    print(event)
    try:
        response = apiHandler(event)
        print(f"response {response}")
        return {
            'statusCode': response['statusCode'],
            'body': json.dumps(response['body']),
            'headers': {
                "Access-Control-Allow-Origin": "*",
            },
        }
    except Exception as e:
        print(f"lambda exception: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps(e)
        }