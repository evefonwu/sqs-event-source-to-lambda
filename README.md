# SQS Event Source to Lambda Function Demo

This is the CDK Python Application source code for the demo described in this post:

[EDA Point-to-point Messaging: SQS Event Source to Lambda Function Demo](https://dev.to/evefonwu/eda-messaging-sqs-event-source-to-lambda-function-demo-30gb)

## Steps

### Requirements

For system requirements to deploy CDK applications, check out: [Tutorials](https://docs.aws.amazon.com/cdk/v2/guide/serverless_example.html)

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
