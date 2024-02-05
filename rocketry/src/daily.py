import requests as rq

path = 'weather'
# path = '127.0.0.1'

def check_collector_api():
    return rq.get(f'http://{path}:5018/ping').content

def check_kernel_api():
    return rq.get(f'http://{path}:5008/ping').content

def test_collect_station():
    req = rq.post(f'http://{path}:5018/collect_station',json={'station_code':'A612'})
    return req

def make_request_to_collect_data():
    req = rq.post(f'http://{path}:5008/collect_all')
    return req

def send_request_to_seleniumAPI_to_collect_station():
    try:
        return make_request_to_collect_data()
    except:
        return 'ERR: failed'
