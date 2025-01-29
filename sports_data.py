import requests
import os
import json
from dotenv import load_dotenv


def main():

    load_dotenv()
    api_key = os.getenv("SPORTS_DATA_API_KEY")
    url = "https://replay.sportsdata.io/api/v4/soccer/odds/json/alternatemarketgameoddsbydate/epl/2023-09-23?key="+api_key  # Add the URL for the GET request to sportsdata.io
    response = requests.get(url)
    if response.status_code == 200:
        with open('response.json', 'w') as file:
            file.write(response.text)
    else:
        print(f"Failed to retrieve data: {response.status_code}")

if __name__ == "__main__":
    main()
