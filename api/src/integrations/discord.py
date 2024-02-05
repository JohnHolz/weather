from requests import post

def send_mensage_on_bot_channel_as_weather_bot(mensage):
    webhook_url = 'https://discord.com/api/webhooks/1192921272800264364/lomMNo3iWZypgeN0-cGd5TSBAWaRJiIIRGWC5ckU_qICKflAqZ928jTc_dQShTBWHiev'
    json_data = {'content':mensage}
    req = post(webhook_url, json=json_data)
    return req

def make_message():
    return f"""----------------------------"""
