

import requests as rq 


req = rq.post('http://localhost:5008/collector', json={'station':'A612'})
print(req.json())

response = {
    'status': 200,
    'message': 'Success',
    'data': {
        'station': 'A612',
        'city': 'Vitoria',
        'state': 'ES',
        'temperatures': [{'date':'01/04/2024',
                          'hour':'01:00',
                          'temperature':23.5}],
    }
}