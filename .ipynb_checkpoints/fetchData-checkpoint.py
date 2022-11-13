import urllib.request
from datetime import date

today = date.today()

d1 = today.strftime("%d/%m/%Y")
urllib.request.urlretrieve('https://data.sensor.community/static/v2/data.24h.json', f'data.24h-{d1}.json')
