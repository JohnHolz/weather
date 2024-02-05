import pytest
import requests as rq

# path = 'weather'
path = '127.0.0.1'

def test_collect_all():
    response = rq.post(f'http://{path}:5008/collect_all')
    assert response.status_code == 200

def test_reset_stations_table():
    response = rq.get(f'http://{path}:5008/reset_stations_table')
    assert response.status_code == 200

def test_patch_station():
    response = rq.patch(f'http://{path}:5008/deactivate_station', json={'station_code': 'A612'})
    assert response.status_code == 200
    response = rq.patch(f'http://{path}:5008/activate_station', json={'station_code': 'A612'})
    assert response.status_code == 200

def test_patch_state():
    response = rq.patch(f'http://{path}:5008/deactivate_state', json={'state_code': 'ES'})
    assert response.status_code == 200
    response = rq.patch(f'http://{path}:5008/activate_state', json={'state_code': 'ES'})
    assert response.status_code == 200

def test_state_stations():
    response = rq.get(f'http://{path}:5008/state_stations', json={'state_code': 'ES'})
    assert response.status_code == 200

def test_ping():
    response = rq.get(f'http://{path}:5008/ping')
    assert response.status_code == 200

def test_third_party():
    response = rq.patch(f'http://{path}:5018/collect_station', json={'station_code': 'A612'})
    assert response.status_code == 200

def main():
    test_reset_stations_table()
    test_patch_station()
    test_patch_state()

    test_third_party()
    test_state_stations()
    test_ping()
    test_collect_all()

if __name__ == "__main__":
    main()