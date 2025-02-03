class AlternateMarketPregameOdds:
    def __init__(self, game_odd_id, sportsbook, game_id, created, 
                 updated, home_money_line, away_money_line, 
                 draw_money_line, home_point_spread, away_point_spread,
                 home_point_spread_payout, away_point_spread_payout,
                 over_under, over_payout, under_payout, sportsbook_id, 
                 sportsbook_url, home_team_asian_handicap, away_team_asian_handicap, 
                 home_team_asian_handicap_payout, away_team_asian_handicap_payout, 
                 asian_total, asian_total_over_payout, asian_total_under_payout, odd_type):
        
        self.game_odd_id = game_odd_id
        self.sportsbook = sportsbook
        self.game_id = game_id
        self.created = created
        self.updated = updated
        self.home_money_line = home_money_line
        self.away_money_line = away_money_line
        self.draw_money_line = draw_money_line
        self.home_point_spread = home_point_spread
        self.away_point_spread = away_point_spread
        self.home_point_spread_payout = home_point_spread_payout
        self.away_point_spread_payout = away_point_spread_payout
        self.over_under = over_under
        self.over_payout = over_payout
        self.under_payout = under_payout
        self.sportsbook_id = sportsbook_id
        self.sportsbook_url = sportsbook_url
        self.home_team_asian_handicap = home_team_asian_handicap
        self.away_team_asian_handicap = away_team_asian_handicap
        self.home_team_asian_handicap_payout = home_team_asian_handicap_payout
        self.away_team_asian_handicap_payout = away_team_asian_handicap_payout
        self.asian_total = asian_total
        self.asian_total_over_payout = asian_total_over_payout
        self.asian_total_under_payout = asian_total_under_payout
        self.odd_type = odd_type
    
