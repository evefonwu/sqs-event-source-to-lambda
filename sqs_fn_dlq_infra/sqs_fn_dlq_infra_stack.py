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
        Message SQS queue with a DLQ
        '''
        message_dql = sqs.DeadLetterQueue(
            max_receive_count=10,
            queue=sqs.Queue(self, 'MessageDQLQueue', 
                retention_period=Duration.days(14))
        )
        message_queue = sqs.Queue(self, "MessageQueue",
            visibility_timeout=Duration.seconds(300),
            dead_letter_queue=message_dql,                
        )
        
        '''
        Function with sqsEventSource to poll for SQS messages 
        '''
        current_dir = os.path.dirname(__file__)
        lambdaDirectory = os.path.join(current_dir, '../lambda')                
        
        processorFn = _lambda.Function(self, "ProcessorFn",
            code=_lambda.Code.from_asset(lambdaDirectory),
            handler="processor.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            retry_attempts=2, 
            environment={
                'MESSAGE_QUEUE_URL': message_queue.queue_url
            }
        )

        processorFn.add_event_source(lambda_es.SqsEventSource(message_queue))

        '''
        FunctionURL to simulate sending a message to the queue
        '''
        sender_fn = _lambda.Function(self, "SenderFn",
            code=_lambda.Code.from_asset(lambdaDirectory),
            handler="sender.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            environment={
                'SQS_QUEUE_URL': message_queue.queue_url
            }
        )        
        fn_url = sender_fn.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,
            cors=_lambda.FunctionUrlCorsOptions(
                allowed_origins=["*"], 
                allowed_methods=[_lambda.HttpMethod.ALL],
                allowed_headers=["*"]
            )
        )

        '''
        Permissions for sender_fn to send messages to the queue
        '''
        message_queue.grant_send_messages(sender_fn)

        '''
        CfnOutputs
        '''
        CfnOutput(self, "SenderFn_URL", value=fn_url.url)
