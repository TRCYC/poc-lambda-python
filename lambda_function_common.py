import logging
import os
import sys
import pytz

# Define the timezone (e.g., UTC)
TIMEZONE_UTC = pytz.utc

# Define the Eastern Time timezone (handles both EST and EDT)
TIMEZONE_EST = pytz.timezone('America/New_York')

# Get the log level from the environment variable, default to 'DEBUG' if not set
LOG_LEVEL = os.getenv('LOGLEVEL', 'DEBUG').upper()

def initialize_logging(message_id, log_level, lambda_function_name):
    # Access the root logger
    root_logger = logging.getLogger()
    log_level = getattr(logging, log_level, logging.DEBUG)
    root_logger.setLevel(log_level)

    # Create a formatter with message_id
    formatter = logging.Formatter(f'{lambda_function_name}::%(levelname)s::%(message_id)s::%(message)s\n')

    # Check if the root logger already has handlers
    if not root_logger.handlers:
        # Create a stream handler if no handlers exist
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(formatter)
        root_logger.addHandler(stream_handler)

    # Add the message ID to each log record
    for handler in root_logger.handlers:
        handler.addFilter(lambda record: setattr(record, 'message_id', message_id) or True)

    # Suppress Boto3 and Botocore logs
    logging.getLogger('boto3').setLevel(logging.WARNING)
    logging.getLogger('botocore').setLevel(logging.WARNING)
    logging.getLogger('aws_lambda').setLevel(logging.WARNING)
    logging.getLogger('msal').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)