import requests as rq

def check_api():
    return rq.get('http://192.168.0.14:5018/ping').content
