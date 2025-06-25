FROM public.ecr.aws/lambda/python:3.12

# Install necessary packages
RUN microdnf install -y libaio wget unzip && microdnf clean all

# Download and install Oracle Instant Client
RUN wget https://download.oracle.com/otn_software/linux/instantclient/2350000/instantclient-basic-linux.x64-23.5.0.24.07.zip && \
    unzip instantclient-basic-linux.x64-23.5.0.24.07.zip -d /opt/oracle && \
    rm instantclient-basic-linux.x64-23.5.0.24.07.zip

# Set environment variables for Oracle Instant Client
ENV ORACLE_HOME=/opt/oracle/instantclient_23_5
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_23_5:$LD_LIBRARY_PATH
ENV PATH=/opt/oracle/instantclient_23_5:$PATH

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