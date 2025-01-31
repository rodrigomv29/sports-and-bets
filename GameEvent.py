class GameEvent:
    def __init__(self, season, week, date_time, status, 
                 away_team_id, home_team_id, away_team_name, 
                 home_team_name, away_team_score, home_team_score, 
                 total_score, pre_game_odds=[], live_odds=[]):
        self.season = season
        self.week = week
        self.date_time = date_time
        self.status = status
        self.away_team_id = away_team_id
        self.home_team_id = home_team_id
        self.away_team_name = away_team_name
        self.home_team_name = home_team_name
        self.away_team_score = away_team_score
        self.home_team_score = home_team_score
        self.total_score = total_score
        self.pre_game_odds = pre_game_odds
        self.live_odds = live_odds
