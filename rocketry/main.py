from rocketry import Rocketry
import os
from src.daily import send_request_to_seleniumAPI_to_collect_station, check_kernel_api, check_collector_api
from rocketry.conds import daily, hourly, time_of_day
import random
from datetime import datetime

def write_string_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
        file.close()

app = Rocketry()

@app.task(daily &  time_of_day.between('23:05', '23:35'))
def do_daily():
    os.system('echo !!! daily work !!!')
    echo =  send_request_to_seleniumAPI_to_collect_station()
    os.system(f"echo {echo.status_code}:{echo.content}")

@app.task(hourly)
def do_hourly():
    log = {}
    random_number = random.randint(1000, 12000)
    log['kernel'] = check_kernel_api()
    log['collector'] = check_collector_api()
    log['current_time'] = datetime.now().time().hour

    os.system(f'echo !!! {random_number}{log["current_time"]}')
    print('hourly')

if __name__ == '__main__':
    app.run()