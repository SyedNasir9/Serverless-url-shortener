import json
import random
import string

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        long_url = body.get("url")
        
        if not long_url:
            raise ValueError("URL is required")

        # Generate a random short code (6 characters)
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        # For simplicity, assume you are saving the mapping to S3
        # s3.put_object(Bucket='your-bucket-name', Key=f'short_codes/{short_code}', Body=long_url)

        # Return the shortened URL
        response = {
            "short_url": f"https://your-api-id.execute-api.region.amazonaws.com/prod/{short_code}"
        }

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS"
            },
            "body": json.dumps(response)
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS"
            },
            "body": json.dumps({"error": str(e)})
        }
