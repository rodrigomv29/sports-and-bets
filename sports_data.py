import requests
import os
import json
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("SPORTS_DATA_API_KEY")
    url = "https://replay.sportsdata.io/api/v4/soccer/odds/json/alternatemarketgameoddsbydate/epl/2023-09-23?key="+api_key  # Add the URL for the GET request to sportsdata.io
    response = requests.get(url)
    res_data = response.json()    
    res_data[0].pop('GameId')
    res_data[0].pop('RoundId')
    res_data[0].pop('SeasonType')
    res_data[0].pop('Day')
    res_data[0].pop('GlobalGameId')
    res_data[0].pop('GlobalAwayTeamId')
    res_data[0].pop('GlobalHomeTeamId')
    if response.status_code == 200:
        with open('response.json', 'w') as file:
            print('writing to file')
            file.write(str(res_data))
    else:
        print(f"Failed to retrieve data: {response.status_code}")