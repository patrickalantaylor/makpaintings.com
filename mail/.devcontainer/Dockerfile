FROM mcr.microsoft.com/devcontainers/python:3.12

# Install AWS CLI v2
RUN apt-get update && \
    apt-get install -y unzip curl groff less && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Install AWS SAM CLI
RUN pip install aws-sam-cli

# Install boto3 (for Lambda dev)
RUN pip install boto3
