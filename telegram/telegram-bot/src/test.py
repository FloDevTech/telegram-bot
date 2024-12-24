import requests

payload = dict(key1='value1', key2='value2')
r = requests.get("http://localhost:5678/webhook-test/c5c1757f-bffd-41ed-8af9-72d8aec5409b",json=payload)