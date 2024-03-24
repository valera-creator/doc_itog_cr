import requests

port = 5000
host = '127.0.0.1'
url = f'https://{host}:{port}'  # не забываем https://
response = requests.get(url)
data_get = response.json()
