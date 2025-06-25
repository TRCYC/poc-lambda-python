import os
os.environ['env'] = 'dev'

from lambda_functionSetup import setup_environment
setup_environment()

from lambda_function import lambda_handler

if __name__ == "__main__":
    # Set up the environment
    context = {}  # Add any context data if needed
    event ={}
    event = {"file_move_only": "yes"}

    
    lambda_handler(event, context)