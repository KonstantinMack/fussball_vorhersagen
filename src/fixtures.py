import pandas as pd
import numpy as np
from massey_prediction import massey_prediction_main
from helper_fcts import preprocess, get_probs, get_bookie_probs
from stats2 import get_stats2
from exp_goals_poisson import get_poisson
from momentum import get_momentum


def get_data(league):
    df = pd.read_csv(f"http://www.football-data.co.uk/mmz4281/1819/{league}.csv")
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
