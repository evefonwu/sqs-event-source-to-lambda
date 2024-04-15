import os 
from aws_cdk import (
    Duration,
    CfnOutput,
    Stack,    
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_es,
)
from constructs import Construct

class SqsFnDlqInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        '''
        Original message queue 
        - with a DLQ to store undeliverable messages 
        '''
        message_dql = sqs.DeadLetterQueue(
            max_receive_count=10,
            queue=sqs.Queue(self, 'MessageDQLQueue', 
                retention_period=Duration.days(14))
        )
        original_queue = sqs.Queue(self, "OriginalQueue",
            visibility_timeout=Duration.seconds(300),
            dead_letter_queue=message_dql,
            # sqs properties, default batch_size 10
        )
        
        '''
        processor lambda function
        - with sqsEventSource to poll SQS messages for lambda to process
        '''
        current_dir = os.path.dirname(__file__)
        lambdaDirectory = os.path.join(current_dir, '../lambda')                
        
        processorFn = _lambda.Function(self, "ProcessorFn",
            code=_lambda.Code.from_asset(lambdaDirectory),
            handler="processor.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            retry_attempts=2, 
            environment={
                'MESSAGE_QUEUE_URL': original_queue.queue_url
            }
        )

        processorFn.add_event_source(lambda_es.SqsEventSource(original_queue))

        # lambda FunctionURL to simulat sending a message to the original queue
        # CfnOutput(self, "")
