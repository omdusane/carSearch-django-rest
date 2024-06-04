import requests

endpoint = 'http://localhost:8000/car/list'

getresponse = requests.get(endpoint)

print (getresponse.json())
