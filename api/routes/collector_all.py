from jh_utils.data.sql.object import create_object_DB_by_envfile
from flask import request, Blueprint, make_response, jsonify
from src.collect_all import collect_all_stations, station_status_code
#### rota

collect_all_blueprint = Blueprint('collect_all_blueprint', __name__, template_folder='model')

@collect_all_blueprint.route('/collect_all', methods =['POST'])
def try_collect_all_station():
    try:
        ob = create_object_DB_by_envfile('.env')
        engine = ob.engine()
        req2 = collect_all_stations(engine)
        req3 = station_status_code(req2)
        return make_response(req3, 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)


