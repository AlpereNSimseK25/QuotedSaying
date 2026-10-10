#Alıntı sözler

import requests

quoteId = input("Enter quote id: ")
getUrl = f"https://dummyjson.com/quotes/{quoteId}"

getResponse = requests.get(getUrl)

if getResponse.status_code == 200:
    print("Connection successful")
    data = getResponse.json()
    for key, value in data.items():
        print(f"{key.upper()}: {value}")
else:
    print("Connection fail")