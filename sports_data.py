"""
{"Season": 
 "Week":
 "DateTime":
 "Status":
 "AwayTeamId": 
 "HomeTeamId": 
 "AwayTeamName": "Nottingham Forest FC", "HomeTeamName": "Manchester City FC", "HomeTeamScore": 2, "AwayTeamScore": 0, "TotalScore": 2,
"""
import requests
import os
import json
from dotenv import load_dotenv

def get_game_title(home, away):
    return home + " is facing " + away 

def get_odds(res):
    home_money_line = res["AlternateMarketPregameOdds"][0]["HomeMoneyLine"]
    away_money_line = res["AlternateMarketPregameOdds"][0]["AwayMoneyLine"]
    home_money_int = int(home_money_line)
    away_money_int = int(away_money_line)
    if min(home_money_int, away_money_int) == home_money_int:
        ret_str = res["HomeTeamName"] + " is the favorite at " + str(min(home_money_int, away_money_int)) +"\n"
        ret_str += res["AwayTeamName"] + " is the underdog at +" + str(away_money_int)
    else:
        ret_str = res["AwayTeamName"] + " is the favorite at " + str(min(home_money_int, away_money_int)) +"\n"
        ret_str += res["HomeTeamName"] + " is the underdog at +" + str(home_money_int)
    return ret_str

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
            json.dump(res_data, file, indent=4)
            for i in range(len(res_data)):
                print(get_odds(res_data[i]))
    else:
        print(f"Failed to retrieve data: {response.status_code}")


