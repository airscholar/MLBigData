from datetime import date
import os
import requests

today = date.today()

d1 = today.strftime("%d-%m-%Y")


def download(url):
    get_response = requests.get(url, stream=True)
    file_name = url.split("/")[-1]
    name = '.'.join(file_name.split(".")[:2])
    ext = file_name.split(".")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
        os.rename(file_name, f'datasets/{name}-{d1}.{ext}')


download('https://data.sensor.community/static/v2/data.24h.json')

# %%