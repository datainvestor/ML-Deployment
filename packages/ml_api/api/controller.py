from flask import Blueprint, request


prediction_app = Blueprint('prediction_app', __name__)

#this is one endpoint that when we access we will get 'ok' (routes are defined by @ decorator in flash)
@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'
