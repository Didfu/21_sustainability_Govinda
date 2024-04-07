from flask import Flask
from urllib.request import urlopen
import requests,json
import datetime
from power_generation import PowerPredictionModel
import pandas as pd
apiKey="1437c1a49e68318ce5b003e82942562f"
url='http://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)
cityname=(data.get('city'))
baseURL="https://api.openweathermap.org/data/2.5/weather?q="
completeURL=baseURL+cityname+"&appid="+apiKey
response=requests.get(completeURL)
data2=response.json()
current_time = datetime.datetime.now()
current_datetime = current_time.replace(minute=0, second=0)
formatted_datetime = current_datetime.strftime("%d-%m-%y %H:%M")
WindSpeed=data2['wind']['speed']
AirTemperature=data2['main']['temp']
Pressure=data2['main']['pressure']
df = pd.DataFrame([formatted_datetime, WindSpeed, AirTemperature, Pressure], index=["DateTime", "Wind Speed", "Air Temperature", "Pressure"])


def getData():
    return df