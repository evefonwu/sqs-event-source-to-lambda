import os 
import boto3

'''
This lambda fn sends a message to an SQS queue.
'''

sqs = boto3.client('sqs')

def lambda_handler(event, context):
  queue_url = os.environ.get('SQS_QUEUE_URL')
  print(queue_url)

  params = {
    'MessageBody': 'Hello Queue!',
    'QueueUrl': queue_url,    
  }

  try: 
    response = sqs.send_message(**params)
    
    message_id = response.get('MessageId')
    if message_id:
      print(f"Published message. Message ID: {message_id}")      
    else:
      print(f"Failed to send message to SQS queue: {queue_url}")

  except Exception as e:
    print(f"Failed sns.publish: {e}")
  
  

