# SQS Event Source to Lambda Function Demo

Demo of Amazon Simple Queue Service (SQS) queue as event source to an AWS Lambda function.

## Steps

### Requirements

Requirements for any CDK app, in general, check out: [Getting Started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

Specific to CDK apps in Python: [Working with the AWS CDK in Python
](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)

### Clone the repository

cd into the project

### Create a virtual environment with venv

```sh
python3 -m venv .venv
```

### Activate venv environment

```sh
source .venv/bin/activate
```

### Install package dependencies

This repo requires aws-cdk-lib 2.137.0. See requirements.txt for package dependencies.

Install into the venv virtual environment for this project:

```sh
pip install -r requirements.txt
```

### Deploy to AWS account/region

Initiate deploying to the default AWS account/region configured with the AWS CLI

```sh
cdk deploy
```

## Blog post and Resource links:

[EDA Messaging: SQS Event Source to Lambda Function Demo](https://dev.to/evefonwu/eda-messaging-sqs-event-source-to-lambda-function-demo-30gb)
