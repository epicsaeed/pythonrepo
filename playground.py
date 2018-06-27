import requests

url = 'http://127.0.0.1:9214/products/'

r = requests.get(url)

print(r.json())
print(r.headers['content-type'])