import boto3 
import os 

'''
This lambda receives messages polled from an SQS event source 
and deletes the message from the queue after logging out the
message payload.
'''

sqs = boto3.client('sqs')

def lambda_handler(event, context):
  print(event)
  
  message_queue_url = os.environ.get('MESSAGE_QUEUE_URL')
  if event.get('Records'):
    for record in event.get('Records'):
      payload = record.get('body')
      if payload:
        print(str(payload))

      receipt_handle = record.get('receiptHandle') 
      params = {
        'QueueUrl': message_queue_url,
        'ReceiptHandle': receipt_handle,
      }
      sqs.delete_message(**params)
    
  else: 
    print('Lambda triggered to execute but there are no SQS records')

  
