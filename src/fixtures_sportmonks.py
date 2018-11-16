
import datetime
import numpy as np
import os
import pandas as pd
import pickle
import requests as re

from fixtures import help_step, add_ratings, get_exp_goals, poi_mas_mix
from helper_fcts import get_bookie_probs
from massey_prediction import massey_prediction_main


PATH = "C:\\Users\\Konny\\DataScience\\SpicedAcademy\\fussball_vorhersagen\\src\\"

API = os.getenv('SPORTMONKS')

DATE = datetime.datetime.now().strftime("%d-%m-%y")

COLS = ['H_avgGD', 'A_avgGD', 'H_avgG', 'A_avgG', 'H_avgG_c', 'A_avgG_c', 'H_avgST', 'A_avgST', 'H_avgST_c', 'A_avgST_c', 'H_avgC', 'A_avgC', 'H_avgC_c', 'A_avgC_c', 'H_GoalDiff_last', 'A_GoalDiff_last', 'H_xG_PoiMas', 'A_xG_PoiMas', 'H_Form_Tot4', 'A_Form_Tot4','H_Def_Rat', 'H_Off_Rat', 'A_Def_Rat', 'A_Off_Rat', "H_prob_odds", "D_prob_odds", "A_prob_odds", "D1", "E0", "E1", "E2", "E3", "F1", "I1", "SP1"]

LEAGUE_MAPPING = {
        "E0": 20,
        "E1": 24,
        "E2": 24,
        "E3": 24,
        "F1": 20,
        "I1": 20,
        "D1": 18,
        "SP1": 20,
        "F2": 20,
        "I2": 20,
        "D2": 18,
        "SP2": 22,
        "B1": 16,
        "G1": 16,
        "N1": 18,
        "P1": 18,
        "T1": 18
        }

MAJOR_LEAGUES = ["D1", "E0", "E1", "E2", "E3", "F1", "I1", "SP1"]
MINOR_LEAGUES = ["D2", "F2", "I2", "SP2", "B1", "G1", "N1", "P1", "T1"]


def load_obj(name):
    with open('C:/Users/Konny/DataScience/SpicedAcademy/fussball_vorhersagen/src/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


leagues_dict = load_obj("leagues_dict")
teams_dict_reverse = load_obj("teams_dict_reverse")


def get_fixtures_by_date(date1, date2):
    url = f"https://soccer.sportmonks.com/api/v2.0/fixtures/between/{date1}/{date2}?api_token={API}&include=localTeam.venue,visitorTeam.venue,league,flatOdds:filter(bookmaker_id|70)"
    fixtures = re.get(url).json()
    pages = fixtures["meta"]["pagination"]["total_pages"]
    if pages > 1:
        fix_list = fixtures["data"]
        for page in range(2,pages+1):
            url2 = url + f"&page={page}"
            next_page = re.get(url2).json()["data"]
            fix_list += next_page
        return fix_list
    return fixtures["data"]


def get_odds_by_fix_id(fix_id, market, bookie_id=2):
    url = f"https://soccer.sportmonks.com/api/v2.0/odds/fixture/{fix_id}/bookmaker/{bookie_id}?api_token={API}"
    try:
        data = re.get(url).json()["data"]
        odds = [x["bookmaker"]["data"][0]["odds"]["data"] for x in data if x["id"] == market]
        return odds
    except:
        return []


def get_hc_odds(odds_list, fix_id):
    odds = [x["odds"] for x in odds_list if x["market_id"] == 28]
    bookie = "Pin"
    if not odds:
        odds = get_odds_by_fix_id(fix_id, 28)
        bookie = "Bet365"
    if not odds:
        return np.NaN, np.NaN, np.NaN, np.NaN, np.NaN
    try:
        df = pd.DataFrame(odds[0])["handicap label value".split()]
        df = df.applymap(float)
        df["diff2"] = (df.value - 1.96)**2
        mini = df.iloc[df.diff2.values.argmin()]
        aprx_hc = mini["handicap"] + (mini["value"] - 1.96) / 1.2
        hc = mini.handicap
        opp = mini.label % 2 + 1
        opp_odds = float(df.loc[(df["handicap"] == -hc) & (df["label"] == opp), "value"])
        if mini.label == 1:
            return hc, round(aprx_hc, 2), mini.value, opp_odds, bookie
        else:
            return -hc, round(-aprx_hc, 2), opp_odds, mini.value, bookie
    except:
        return np.NaN, np.NaN, np.NaN, np.NaN, np.NaN


def get_1x2_odds(odds_list, fix_id):
    odds = [x["odds"] for x in odds_list if x["market_id"] == 1]
    bookie = "Pin"
    if not odds:
        odds = get_odds_by_fix_id(fix_id, 1)
        bookie = "Bet365"
    if not odds:
        return np.NaN, np.NaN, np.NaN, np.NaN
    odds_dict = {x["label"]: float(x["value"]) for x in odds[0]}
    return odds_dict["1"], odds_dict["X"], odds_dict["2"], bookie


def get_relevant_info(fix_list):
    fixtures = []
    for fix in fix_list:
        fix_data = {}
        fix_data["fix_id"] = fix["id"]
        fix_data["timestamp"] = fix["time"]["starting_at"]["timestamp"]
        fix_data["League_id"] = fix['league']["data"]["id"]
        fix_data["HomeTeam"] = fix['localTeam']['data']['name']
        fix_data["AwayTeam"] = fix['visitorTeam']['data']['name']
        ahc_odds = get_hc_odds(fix["flatOdds"].get("data", []), fix["id"])
        fix_data["BbAHh"] = ahc_odds[0]
        fix_data["aprx_HC"] = ahc_odds[1]
        fix_data["BbMxAHH"] = ahc_odds[2]
        fix_data["BbMxAHA"] = ahc_odds[3]
        fix_data["BbAvAHH"] = ahc_odds[2]
        fix_data["BbAvAHA"] = ahc_odds[3]
        odds = get_1x2_odds(fix["flatOdds"].get("data", []), fix["id"])
        fix_data["BbMxH"] = odds[0]
        fix_data["BbMxD"] = odds[1]
        fix_data["BbMxA"] = odds[2]
        fix_data["BbAvH"] = odds[0]
        fix_data["BbAvD"] = odds[1]
        fix_data["BbAvA"] = odds[2]
        fixtures.append(fix_data)
    return fixtures


def get_new_fixtures_by_date(date1, date2):
    fix_data = get_fixtures_by_date(date1, date2)
    fixtures = get_relevant_info(fix_data)
    df = pd.DataFrame(fixtures)
    df["Div"] = df.League_id.map(leagues_dict)
    df["Date"] = pd.to_datetime(df.timestamp, unit="s").dt.strftime('%Y/%m/%d %H:%M')
    df["HomeTeam"] = df.HomeTeam.map(teams_dict_reverse)
    df["AwayTeam"] = df.AwayTeam.map(teams_dict_reverse)
    return df


def get_new_matches(league, fixs_df):
    """
    Processes the new fixtures
    """
    print(f"processing league: {league}")
    df = pd.read_csv(f"http://www.football-data.co.uk/mmz4281/1819/{league}.csv")
    df["HomeTeam"] = df["HomeTeam"].apply(str.strip)
    df["AwayTeam"] = df["AwayTeam"].apply(str.strip)
    fixs = fixs_df.loc[fixs_df["Div"] == league]
    num_teams = LEAGUE_MAPPING[league]
    rat_off, rat_def, rat_hfa = massey_prediction_main(df, num_teams)
    df_new = pd.concat([df, fixs]).reset_index(drop=True)
    df_new = help_step(df_new, num_teams//2)
    df_new = add_ratings(df_new, rat_off, rat_def, rat_hfa)
    df_new = poi_mas_mix(get_exp_goals(df_new))
    del df_new["PSCH"]
    del df_new["PSCD"]
    del df_new["PSCA"]
    df_new = get_bookie_probs(df_new)
    if league in MAJOR_LEAGUES:
        for country in MAJOR_LEAGUES:
            if country == league:
                df_new[country] = 1
            else:
                df_new[country] = 0
    return df_new


def get_fixtures_sportsmonks(date1, date2):
    """
    Main function to get new fixtures for minor leagues
    """
    fixtures = get_new_fixtures_by_date(date1, date2)
    leagues = list(set(fixtures.Div.unique()).intersection(set(MAJOR_LEAGUES)))
    if leagues:
        fix_list = [get_new_matches(lg, fixtures) for lg in leagues]
        df = pd.concat(fix_list).reset_index(drop=True)
        df = df[df.Date > date1]
        df = df.loc[df[COLS].dropna().index].reset_index(drop=True)
        return df
    else:
        return pd.DataFrame()


def get_fixtures_other_sportsmonks(date1, date2):
    """
    Main function to get new fixtures for minor leagues
    """
    fixtures = get_new_fixtures_by_date(date1, date2)
    leagues = list(set(fixtures.Div.unique()).intersection(set(MINOR_LEAGUES)))
    if leagues:
        fix_list = [get_new_matches(lg, fixtures) for lg in leagues]
        df = pd.concat(fix_list).reset_index(drop=True)
        df = df[df.Date > date1]
        df = df.loc[df[COLS[:-8]].dropna().index].reset_index(drop=True)
        return df
    else:
        return pd.DataFrame()
