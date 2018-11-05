
import datetime
import numpy as np
import pandas as pd

from exp_goals_poisson import get_poisson
from helper_fcts import preprocess, get_probs, get_bookie_probs
from massey_prediction import massey_prediction_main
from momentum import get_momentum
from stats2 import get_stats2


PATH = "C:\\Users\\Konny\\DataScience\\SpicedAcademy\\fussball_vorhersagen\\src\\"
DATE = datetime.datetime.now().strftime("%d-%m-%y")
COLS = ['H_avgGD', 'A_avgGD', 'H_avgG', 'A_avgG', 'H_avgG_c', 'A_avgG_c', 'H_avgST', 'A_avgST', 'H_avgST_c', 'A_avgST_c', 'H_avgC', 'A_avgC', 'H_avgC_c', 'A_avgC_c', 'H_GoalDiff_last', 'A_GoalDiff_last', 'H_xG_PoiMas', 'A_xG_PoiMas', 'H_Form_Tot4', 'A_Form_Tot4','H_Def_Rat', 'H_Off_Rat', 'A_Def_Rat', 'A_Off_Rat', "H_prob_odds", "D_prob_odds", "A_prob_odds", "D1", "E0", "E1", "E2", "E3", "F1", "I1", "SP1"]


def get_data(league):
    df = pd.read_csv(f"http://www.football-data.co.uk/mmz4281/1819/{league}.csv")
    df["HomeTeam"] = df["HomeTeam"].apply(str.strip)
    df["AwayTeam"] = df["AwayTeam"].apply(str.strip)
    fixtures = pd.read_csv("http://www.football-data.co.uk/fixtures.csv")
    cols = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'BbMxH', 'BbAvH', 'BbMxD',
            'BbAvD', 'BbMxA', 'BbAvA', 'BbOU', 'BbMx>2.5', 'BbAv>2.5',
            'BbMx<2.5', 'BbAv<2.5', 'BbAH', 'BbAHh', 'BbMxAHH', 'BbAvAHH',
            'BbMxAHA', 'BbAvAHA']
    fixs = fixtures[fixtures["Div"] == league][cols]
    return df, fixs


def help_step(df_new, matches):
    df_new = preprocess(df_new)
    df_new = get_momentum(df_new)
    df_new = get_stats2(df_new, 6, 4)
    df_new = get_poisson(df_new, "MIX")
    return df_new[-matches:]


def add_ratings(df, rat_off, rat_def, rat_hfa):
    df["H_Off_Rat"] = df["HomeTeam"].map(rat_off)
    df["H_Def_Rat"] = df["HomeTeam"].map(rat_def)
    df["A_Off_Rat"] = df["AwayTeam"].map(rat_off)
    df["A_Def_Rat"] = df["AwayTeam"].map(rat_def)
    df["HFA"] = rat_hfa
    return df


def get_exp_goals(df):
    """
    Calculates expected home and away goals from Massey Ratings
    """
    df["H_xG_Mas"] = np.where(df["H_Off_Rat"] - df["A_Def_Rat"] + df["HFA"] > 0, df["H_Off_Rat"] - df["A_Def_Rat"] + df["HFA"], 0)
    df["A_xG_Mas"] = np.where(df["A_Off_Rat"] - df["H_Def_Rat"] > 0, df["A_Off_Rat"] - df["H_Def_Rat"], 0)
    df["xGD_Mas"] = df["H_xG_Mas"] - df["A_xG_Mas"]
    return df


def poi_mas_mix(df):
    df["H_xG_PoiMas"] = (df['H_xG_Poi_mix'] + df['H_xG_Mas']) / 2
    df["A_xG_PoiMas"] = (df['A_xG_Poi_mix'] + df['A_xG_Mas']) / 2
    df["H_pred_PoiMas"], df["D_pred_PoiMas"], df["A_pred_PoiMas"], df["O_pred_PoiMas"], df["U_pred_PoiMas"] = get_probs(df["H_xG_PoiMas"], df["A_xG_PoiMas"])
    return df


def get_new_matches(league, num_teams):
    print(f"processing league: {league}")
    df, fixs = get_data(league)
    rat_off, rat_def, rat_hfa = massey_prediction_main(df, num_teams)
    df_new = pd.concat([df, fixs]).reset_index(drop=True)
    df_new = help_step(df_new, num_teams//2)
    df_new = add_ratings(df_new, rat_off, rat_def, rat_hfa)
    df_new = poi_mas_mix(get_exp_goals(df_new))
    del df_new["PSCH"]
    del df_new["PSCD"]
    del df_new["PSCA"]
    df_new = get_bookie_probs(df_new)
    return df_new


def get_matches(league):

    league_mapping = {
        "E0": 20,
        "E1": 24,
        "E2": 24,
        "E3": 24,
        "F1": 20,
        "I1": 20,
        "D1": 18,
        "SP1": 20
        }

    df = get_new_matches(league, league_mapping[league])
    for country in league_mapping.keys():
        if country == league:
            df[country] = 1
        else:
            df[country] = 0
    return df


def get_fixtures():
    fixtures = pd.read_csv("http://www.football-data.co.uk/fixtures.csv")
    fixtures.to_csv(PATH + f"data\\fixtures\\fixtures_{DATE}.csv")
    leagues = list(set(fixtures.Div.unique()).intersection(set(["D1", "E0", "E1", "E2", "F1", "I1", "SP1"]))) #E3 rausgenommen
    fix_list = [get_matches(lg) for lg in leagues]

    df = pd.concat(fix_list).reset_index(drop=True)
    df = df.loc[df[COLS].dropna().index].reset_index(drop=True)
    return df


def get_matches_other(league):

    league_mapping = {
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

    df = get_new_matches(league, league_mapping[league])
    return df


def get_fixtures_other():
    fixtures = pd.read_csv("http://www.football-data.co.uk/fixtures.csv")
    leagues = list(set(fixtures.Div.unique()).intersection(set(["D2", "F2", "I2", "SP2", "B1", "G1", "N1", "P1", "T1"])))
    fix_list = [get_matches_other(lg) for lg in leagues]

    df = pd.concat(fix_list).reset_index(drop=True)
    df = df.loc[df[COLS[:-8]].dropna().index].reset_index(drop=True)
    return df
