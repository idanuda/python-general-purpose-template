from flask import make_response, Blueprint, request

monitor_controller = Blueprint('monitor_controller', __name__, template_folder='templates')

@monitor_controller.route('/api/v1/health-check', methods=(['GET']))
def health_check():
    return make_response(
        {'Health check': 'status ok'},
        200
    )
