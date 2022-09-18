from repositories1.sqs_sender import send_msg


def send_event_to_queue(data):
    return send_msg(data)
