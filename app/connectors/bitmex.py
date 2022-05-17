import requests

def bitmex_contracts():
    contracts = []
    response = requests.get('https://www.bitmex.com/api/v1/instrument/active')
    for item in response.json():
        contracts.append(item['symbol'])
    return contracts

print(bitmex_contracts())