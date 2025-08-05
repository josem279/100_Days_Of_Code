import requests
import os
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 44.34,
    "lon": 10.99,
    "appid": api_key
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = (client.messages
               .create(
                   body="Its going to rain today. Bring an umbrella.",
                   from_= "+<YOUR NUMBER>",
                   to="<ANOTHER NUMBER>"
               ))

    print(message.status)