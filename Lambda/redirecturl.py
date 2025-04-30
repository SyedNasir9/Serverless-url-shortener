import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'syed-url-shortener'  # ✅ your actual bucket name

    try:
        short_code = event['pathParameters']['shortcode']
        response = s3.get_object(Bucket=bucket_name, Key=f'short_codes/{short_code}')
        long_url = response['Body'].read().decode('utf-8')

        return {
            "statusCode": 301,
            "headers": {
                "Location": long_url
            },
            "body": ""
        }

    except s3.exceptions.NoSuchKey:
        return {
            "statusCode": 404,
            "body": "Short URL not found."
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
