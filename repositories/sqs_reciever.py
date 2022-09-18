import boto3
from decouple import config
from signal import signal, SIGINT, SIGTERM

queue_url = config("QUEUE_URL")

sqs_client = boto3.client('sqs', region_name=config("AWS_REGION_NAME"), aws_access_key_id=config("AWS_ACCESS_KEY"), aws_secret_access_key=config("AWS_SECRET"))


def process_message(message_body):
    print(f"processing message: {message_body}")
    # do what you want with the message here
    pass


class SignalHandler:
    def __init__(self):
        self.received_signal = False
        signal(SIGINT, self._signal_handler)
        signal(SIGTERM, self._signal_handler)

    def _signal_handler(self, curr_signal, frame):
        print(f"handling signal {curr_signal}, exiting gracefully")
        self.received_signal = True


signal_handler = SignalHandler()


def consume_messages():
    while not signal_handler.received_signal:
        response = sqs_client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10,
        )
        for message in response.get("Messages", []):
            process_message(message["Body"])


