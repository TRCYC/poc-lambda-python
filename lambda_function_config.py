import os

# Retrieve the Lambda function name from environment variables
LAMBDA_FUNCTION_NAME = os.getenv('LAMBDA_FUNCTION_NAME', 'Cleardox_Entegrate_Reconcile')

# Redshift connection details
REDSHIFT_HOST = os.getenv('REDSHIFT_HOST')
REDSHIFT_PORT = int(os.getenv('REDSHIFT_PORT',5439))
REDSHIFT_DBNAME = os.getenv('REDSHIFT_DBNAME')
REDSHIFT_USER = os.getenv('REDSHIFT_USER')
REDSHIFT_PASSWORD = os.getenv('REDSHIFT_PASSWORD')

# Okta and Cleardox API details
cleardox_client_id = os.getenv('CLEARDOX_CLIENT_ID')
cleardox_client_secret = os.getenv('CLEARDOX_CLIENT_SECRET')
cleardox_token_url = os.getenv('CLEARDOX_TOKEN_URL')
cleardox_data_get_url = os.getenv('CLEARDOX_DATA_GET_URL')
cleardox_data_update_url = os.getenv('CLEARDOX_DATA_UPDATE_URL')
cleardox_document_download_url = os.getenv('CLEARDOX_DOCUMENT_DOWNLOAD_URL')

# Entegrate DB connection details
entegrate_host = os.getenv('ENTEGRATE_HOST')
entegrate_port = int(os.getenv('ENTEGRATE_PORT'))
entegrate_dbname = os.getenv('ENTEGRATE_DBNAME')
entegrate_user = os.getenv('ENTEGRATE_USER')
entegrate_password = os.getenv('ENTEGRATE_PASSWORD')

# Oracle client lib dir
oracle_client_lib = os.getenv('ORACLE_HOME')

# Email Notification Configuration
SEND_EMAIL_FOR_ERRORS = os.getenv('SEND_EMAIL_FOR_ERRORS', 'True').lower() == 'true'
errors = []

# Initialize SNS client
snsTopicARN = os.getenv('SNS_TOPIC_ARN', 'arn:aws:sns:us-east-1:770216840905:etrm-confirms')

# Document type code
documentTypeCode = int(os.getenv('DOCUMENT_TYPE_CODE'))

BUCKET_NAME = os.getenv('BUCKET_NAME', 'etrm-apps')
S3_DIRECTORY = os.getenv('S3_DIRECTORY', 'dev')
FILE_MOVE_URL = os.getenv('FILE_MOVE_URL', '')

# Action Codes
DELETE_ACTION_CODE = 119
SUCCESS_ACTION_CODE = 96