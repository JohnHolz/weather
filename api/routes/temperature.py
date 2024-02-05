from jh_utils.data.sql.object import create_object_DB_by_envfile
from flask import request, Blueprint, make_response, jsonify
from src.collect_all import get_list_of_stations_to_collect
from src.get_values import raw_temperature_data
#### rota

temperature_blueprint = Blueprint('temperature_blueprint', __name__, template_folder='model')

@temperature_blueprint.route('/station', methods =['GET'])
def try_get_station_temperature():
    try:
        data = request.get_json()
        ob = create_object_DB_by_envfile('.env')
        ret_data = raw_temperature_data(data['station_code'], ob.engine())
        return make_response({data['station_code']:ret_data}, 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)


@temperature_blueprint.route('/station/<station_code>', methods =['GET'])
def try_get_one_station_temperature(station_code):
    try:
        ob = create_object_DB_by_envfile('.env')
        ret_data = raw_temperature_data(station_code, ob.engine())
        return make_response({'values':ret_data}, 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)


@temperature_blueprint.route('/state/<state>', methods =['GET'])
def try_get_state_temperature(state):
    try:
        ob = create_object_DB_by_envfile('.env')
        return make_response({"stations":get_list_of_stations_to_collect(ob.engine())}, 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)
