import json
import boto3

def lambda_handler(event, context):
    try:
        short_code = event['pathParameters']['shortcode']
        s3 = boto3.client('s3')

        # Retrieve the long URL using the short code
        response = s3.get_object(Bucket='your-bucket-name', Key=f'short_codes/{short_code}')
        long_url = response['Body'].read().decode('utf-8')

        return {
            "statusCode": 301,
            "headers": {
                "Location": long_url
            }
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
