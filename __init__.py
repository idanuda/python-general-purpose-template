from flask import Flask
import threading
from controllers.entity_controller import entity_controller
from repositories.sqs_reciever import consume_messages

app = Flask(__name__)

# TODO: Add all your controllers here
app.register_blueprint(entity_controller)

if __name__ == "__main__":
   # threading.Thread(target=consume_messages, daemon=True).start()
    app.run(host='0.0.0.0', port=8080)

