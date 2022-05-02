import pandas as pd
import numpy as np

from nba_api.stats.static import teams

all_teams = pd.DataFrame(teams.get_teams())

from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog

def player_game_log(player_id,season):
    '''get player game log'''
    gamelog_player = playergamelog.PlayerGameLog(player_id=player_id,season=season)
    player_game_log = gamelog_player.get_data_frames()[0]
    return player_game_log

from nba_api.stats.endpoints import leaguegamefinder

def team_games(team,season):
    '''get team game log per season'''
    team_id = all_teams[all_teams['abbreviation'] == team]['id']
    team_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=team,season_nullable=season).get_data_frames()[0]
    return team_games

def search_in_team_games():
    '''search in team game log'''
    