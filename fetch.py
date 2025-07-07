import requests
import pandas as pd

url = "https://api.geode-sdk.org/v1"

res = requests.get(url + "/mods")
data = res.json()

for mod in data["payload"]["data"]:
    print({mod["id"]: {
            "download_count": mod["download_count"], 
            "featured": "Sí" if mod["featured"] else "No"
        }
    })



