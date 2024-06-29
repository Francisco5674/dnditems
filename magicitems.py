import requests
import json
import time

url = "https://www.dnd5eapi.co/api/magic-items"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)
data = data["results"]

legendary  = []
veryrare = []
rare = []
uncommon = []

for item in data:
    link = item["url"]
    url = f"https://www.dnd5eapi.co/{link}"
    response = requests.request("GET", url, headers=headers, data=payload)
    magitem = json.loads(response.text)
    rarity = magitem["rarity"]["name"]
    item["rarity"] = rarity
    print(item["name"])
    if rarity == "Uncommon":
        uncommon.append(item)
    elif rarity == "Rare":
        rare.append(item)
    elif rarity == "Very Rare":
        veryrare.append(item)
    elif rarity == "Legendary":
        legendary.append(item)
    time.sleep(0.5)

with open('legendary.json', 'w') as f:
    json.dump(legendary, f)
with open('veryrare.json', 'w') as f:
    json.dump(veryrare, f)
with open('rare.json', 'w') as f:
    json.dump(rare, f)
with open('uncommon.json', 'w') as f:
    json.dump(uncommon, f)

