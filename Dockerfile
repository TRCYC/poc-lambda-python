FROM public.ecr.aws/lambda/python:3.12

# Install necessary packages
RUN microdnf install -y libaio wget unzip && microdnf clean all

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}
COPY lambda_function_common.py ${LAMBDA_TASK_ROOT}
COPY lambda_function_config.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.lambda_handler" ]