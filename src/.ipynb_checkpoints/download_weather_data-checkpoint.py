import requests
import json

api_key = "2G9E678B4VHG4C2YB48CCUFWR"
location = "Nepal"
start_date = "2019-01-01"
end_date = "2022-12-31"

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?unitGroup=metric&key={api_key}&contentType=json"

response = requests.get(url)

print("Status code:", response.status_code)
if response.status_code == 200:
    data = response.json()
    with open("../data/raw/nepal_weather_2019_to_2022.json", "w") as f:
        json.dump(data, f, indent=2)
    print("✅ Data downloaded and saved for February!")
else:
    print("❌ Failed to download. Status:", response.status_code)
