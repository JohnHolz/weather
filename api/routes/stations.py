
from flask import request, Blueprint, make_response, jsonify
from jh_utils.data.pandas.sql import write_sql_table, get_sql_table
from jh_utils.data.sql.object import create_object_DB_by_envfile
import pandas as pd
from src.model import db, Station
from src.stations import write_stations_table,update_state_to_collect, update_state_to_not_collect
from src.collect_all import get_list_of_stations_to_collect, get_stations_as_json_new_data
from src.map_graph import get_map_graph_values
import json

stations_blueprint = Blueprint('base_tables_blueprint', __name__, template_folder='model')

# /state_stations
# /reset_stations_table
# /activate_station
# /deactivate_station
# /activate_station
# /deactivate_station
# /stations_activated

@stations_blueprint.route('/stations_activated', methods =['GET'])
def try_get_stations_been_collected():
    try:
        ob = create_object_DB_by_envfile('.env')
        engine = ob.engine()
        return make_response({"stations":get_list_of_stations_to_collect(engine)}, 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)

@stations_blueprint.route('/stations_graph_map', methods =['GET'])
def try_get_map_graph_values():
    # try:
        ob = create_object_DB_by_envfile('.env')
        engine = ob.engine()
        return make_response(
            jsonify(
                {
                    "stations":json.loads(get_map_graph_values(engine))
                }
            ),
            200)
    # except Exception as e:
        # return make_response(jsonify({"message": "Error"}), 500)


@stations_blueprint.route('/stations_page', methods =['GET'])
def try_get_stations_and_last_value_been_collected():
    try:
        ob = create_object_DB_by_envfile('.env')
        engine = ob.engine()
        return make_response({"stations":get_stations_as_json_new_data(engine)}, 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)

@stations_blueprint.route('/state_stations', methods =['GET'])
def try_get_stations_table():
    try:
        data = request.get_json()
        db_object = create_object_DB_by_envfile()
        df = get_sql_table(query=f"select * from stations where stations.state = '{data['state']}'",
                            engine=db_object.engine())
        return make_response(df.to_json(orient='records'), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)


@stations_blueprint.route('/reset_stations_table', methods =['POST'])
def try_reset_station_table():
    try:
        db_object = create_object_DB_by_envfile()
        ret = write_stations_table(engine=db_object.engine())
        return make_response(jsonify({"message": ret}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)


## station
@stations_blueprint.route('/activate_station', methods =['PATCH'])
def try_update_collect_status_from_station():
    try:
        data = request.get_json()
        station_code = data['station_code']
        station = Station.query.filter_by(station_code=station_code).first()
        station.collect=True
        db.session.add(station)
        db.session.commit()
        return make_response(jsonify({"message": f'{station.station_code}:{station.collect}'}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)

@stations_blueprint.route('/deactivate_station', methods =['PATCH'])
def try_update_to_not_collect_status_from_station():
    try:
        data = request.get_json()
        station_code = data['station_code']
        station = Station.query.filter_by(station_code=station_code).first()
        station.collect=False
        db.session.add(station)
        db.session.commit()
        return make_response(jsonify({"message": f'{station.station_code}:{station.collect}'}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)


## state
@stations_blueprint.route('/activate_state', methods =['PATCH'])
def try_update_collect_status_from_state():
    try:
        data = request.get_json()
        message = update_state_to_collect(data['state'])
        return make_response(jsonify({"message": message}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)


@stations_blueprint.route('/deactivate_state', methods =['PATCH'])
def try_update_to_not_collect_status_from_state():
    try:
        data = request.get_json()
        message = update_state_to_not_collect(data['state'])
        return make_response(jsonify({"message": message}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)