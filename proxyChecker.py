import requests

PROXY = {
    'http': 'http://dtgtsbnu:lmivadwkqvqt@38.154.227.167:5868',
}

r = requests.get('http://httpbin.org/ip', proxies=PROXY)
print(r.json())