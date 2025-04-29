1. Create an API Gateway HTTP API

1.Sign in to the AWS Management Console and navigate to API Gateway.

2.Create a New API:

In the API Gateway dashboard, click Create API.

Select HTTP API and click Build.

Provide the following details:

API Name: URLShortenerAPI

Description: "API for the Serverless URL Shortener"

Stage Name: prod

Click Create API.

2. Set Up Routes for the API
2.1 Create POST Route for Shortening URLs
Go to the Routes section in the API settings.

Click Create to add a new route.

Method: POST

Resource path: /shorten

Integration type: Lambda Function

Select the Lambda function (e.g., shortenurl) that processes the URL shortening.

Enable CORS with these headers:

Access-Control-Allow-Origin: *

Access-Control-Allow-Headers: Content-Type

Access-Control-Allow-Methods: POST, OPTIONS

Click Create.

2.2 Create GET Route for URL Redirection
Create another route for the redirect functionality.

Method: GET

Resource path: /{shortcode}

Integration type: Lambda Function

Select the Lambda function (e.g., redirecturl) for the redirection logic.

Enable CORS with the same headers as the POST route.

Click Create.

3. Integrate Lambda Functions with API Gateway
Each route needs to connect to a Lambda function.

3.1 POST /shorten Route Integration
Integrate the POST route /shorten with the Lambda function (e.g., shortenurl), which will process incoming requests, shorten URLs, and return the shortened URL.

3.2 GET /{shortcode} Route Integration
Integrate the GET route /shortcode with the Lambda function (e.g., redirecturl) that redirects users to the original URL based on the short code.

4. Enable CORS for All Routes
CORS (Cross-Origin Resource Sharing) must be enabled to allow web browsers to make requests to your API from different origins.

In the Routes section, enable CORS for both the POST /shorten and GET /{shortcode} routes.

Add the following headers for both routes:

Access-Control-Allow-Origin: * (or a specific domain if required)

Access-Control-Allow-Headers: Content-Type

Access-Control-Allow-Methods: POST, GET, OPTIONS

5. Deploy the API
Go to the Deployments section in the API Gateway console.

Select the prod stage and click Deploy to make your API live.

6. Test the API
After deployment, use Postman or your browser to test the routes.

6.1 POST /shorten
Make a POST request to /shorten with a JSON body containing the URL to shorten
6.2 GET /{shortcode}
Make a GET request to the shortened URL (e.g., https://your-api-id.execute-api.region.amazonaws.com/prod/abc123) to test if it redirects properly to the original URL.

7. Conclusion
You have now successfully set up API Gateway to handle URL shortening and redirection. With this setup, you can shorten URLs using the POST route and redirect to the original URL using the GET route.

