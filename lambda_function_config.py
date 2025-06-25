import os

# Retrieve the Lambda function name from environment variables
LAMBDA_FUNCTION_NAME = os.getenv('LAMBDA_FUNCTION_NAME', 'poc-python')