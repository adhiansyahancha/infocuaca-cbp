import requests

# Endpoint API cuaca
data_cuaca = requests.get("https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json").json()['row']['data']['forecast']['area']
