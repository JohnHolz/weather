
from flask import request, Blueprint, make_response, jsonify

test_blueprint = Blueprint('test_blueprint', __name__, template_folder='model')

## get 200
@test_blueprint.route('/ping', methods =['GET'])
def try_ping_post():
    return make_response(jsonify({"message": "pong"}), 200)    

## post 200
@test_blueprint.route('/pong', methods =['POST'])
def try_ping_get():
    return make_response(jsonify({"message": "pong"}), 200)