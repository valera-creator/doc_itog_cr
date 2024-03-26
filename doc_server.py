import requests

port = 5000
host = '127.0.0.1'
url = f'http://{host}:{port}'  # не забываем http://, если не робит, то s приписать попробовать
response = requests.get(url)
data_get = response.json()
