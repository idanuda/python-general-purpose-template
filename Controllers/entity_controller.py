from flask import make_response, Blueprint, request
from services.entity_service import send_event_to_queue
from repositories.atlas_connector import get_server_info

entity_controller = Blueprint('entity_controller', __name__, template_folder='templates')


@entity_controller.route('/v0/entities', methods=(['PUT']))
def entities():
    response = send_event_to_queue(request.json)
    return make_response(
        {'status': response},
        200
    )

@entity_controller.route('/v0/atlas', methods=(['GET']))
def atlas_info():
    response = get_server_info(request.args.get('collection_name'), request.args.get('id'))
    return make_response(
        {'info': response},
        200
    )

@entity_controller.route('/api/v1/healthCheck', methods=(['GET']))
def health_check():
    return make_response(
        {'Health check': 'status ok'},
        200
    )
