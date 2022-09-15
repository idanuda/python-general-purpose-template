import boto3, json
from decouple import config

queue_url = config("QUEUE_URL")
sqs_client = boto3.client('sqs', region_name=config("AWS_REGION_NAME"), aws_access_key_id=config("AWS_ACCESS_KEY"),
                          aws_secret_access_key=config("AWS_SECRET"))


def send_msg(data):
    # Send message to SQS queue
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(data),
        MessageGroupId='some-group-id'
    )
    print(response)
    return response


