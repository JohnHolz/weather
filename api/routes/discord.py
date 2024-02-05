from requests import post
from flask import request, Blueprint, make_response, jsonify
from api.src.integrations.discord import send_mensage_on_bot_channel_as_weather_bot

discord_blueprint = Blueprint('discord_blueprint', __name__, template_folder='model')


@discord_blueprint.route('/discord/state_temp', methods =['GET'])
def try_send_discord_mensage():
    try:
        return 200
        # req = send_mensage_on_bot_channel_as_weather_bot(make_message())
        return make_response(jsonify({"message": req.content}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)


@discord_blueprint.route('/discord/station', methods =['GET'])
def try_get_message_value():
    try:
        data = request.get_json()
        return 200
        # return make_response(jsonify({"message": make_message(get_simple_dict(data['simble']))}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)
    
