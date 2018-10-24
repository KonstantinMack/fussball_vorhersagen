
import pandas as pd
import numpy as np
from scipy.stats import poisson
from profit_loss import get_pl


def get_result_encoding(df):
    """
    Creates an encoding for the result
    """
    df["Home"] = np.where(df["FTHG"] > df["FTAG"], 1, 0)
    df["Draw"] = np.where(df["FTHG"] == df["FTAG"], 1, 0)
    df["Away"] = np.where(df["FTHG"] < df["FTAG"], 1, 0)
    df["GoalDiff"] = df["FTHG"] - df["FTAG"]
    df["GoalDiff_Ahc"] = df["GoalDiff"] + df["BbAHh"]
    df["Handicap"] = -df["BbAHh"]
    return df


def make_int_helper(x):
    try:
        x = int(x)
    except:
        x = np.NaN
    return x


def make_ints(df):
    df.dropna(thresh=5, inplace=True)
    cols = ['FTHG', 'FTAG', 'HTHG', 'HTAG', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC','AC', 'HY', 'AY', 'HR', 'AR']
    df[cols] = df[cols].applymap(lambda x: make_int_helper(x))
    return df


def actual_points(df):
    df["H_Pts"] = np.where(df["FTHG"] > df["FTAG"], 3, np.where(df["FTHG"] == df["FTAG"], 1, 0))
    df["A_Pts"] = np.where(df["FTHG"] > df["FTAG"], 0, np.where(df["FTHG"] == df["FTAG"], 1, 3))
    return df


def exp_points(df):
    """
    Calculates expected points for home and away team
    """
    df["H_Pts_Exp"] = 3 * df["H_prob_odds"] + 1 * df["D_prob_odds"]
    df["A_Pts_Exp"] = 3 * df["A_prob_odds"] + 1 * df["D_prob_odds"]
    return df


def won_ahc(row):
    """
    Helper function to determine if teams won against their handicap
    """
    if row["FTHG"] + row["BbAHh"] - row["FTAG"] > 0.25:
        home = 1
        away = 0
        home_win_ahc = 1
        away_win_ahc = -10
    elif row["FTHG"] + row["BbAHh"] - row["FTAG"] == 0.25:
        home = 0.75
        away = 0.25
        home_win_ahc = 1
        away_win_ahc = -10
    elif row["FTHG"] + row["BbAHh"] - row["FTAG"] == 0:
        home = 0.5
        away = 0.5
        home_win_ahc = 0
        away_win_ahc = 0
    elif row["FTHG"] + row["BbAHh"] - row["FTAG"] == -0.25:
        home = 0.25
        away = 0.75
        home_win_ahc = -10
        away_win_ahc = 1
    else:
        home = 0
        away = 1
        home_win_ahc = -10
        away_win_ahc = 1
    return home, away, home_win_ahc, away_win_ahc


def actual_ahc(df):
    df["H_Pts_Ahc"], df["A_Pts_Ahc"], df["H_Win_Ahc"], df["A_Win_Ahc"] = zip(*df.apply(won_ahc, axis=1))
    return df


def exp_ahc(df):
    df["H_Pts_Ahc_Exp"] = df['H_prob_ahc_odds']
    df["A_Pts_Ahc_Exp"] = df['A_prob_ahc_odds']
    return df


def convert_odds(*args):
    """
    Takes odds as input and converts them into probabilities
    """
    inv = [1/i for i in args]
    inv_sum = sum(inv)
    return (i/inv_sum for i in inv)


def get_bookie_probs(df):
    """
    Calculates the outcome probabilities which are implied by the
    bookmaker's odds
    """
    if "PSCH" in df.columns:
        df["H_prob_odds"], df["D_prob_odds"], df["A_prob_odds"] = convert_odds(df["PSCH"], df["PSCD"], df["PSCA"])
    else:
        df["H_prob_odds"], df["D_prob_odds"], df["A_prob_odds"] = convert_odds(df["BbAvH"], df["BbAvD"], df["BbAvA"])

    df["H_prob_ahc_odds"], df["A_prob_ahc_odds"] = convert_odds(df['BbAvAHH'], df['BbAvAHA'])
    df["Over_prob_odds"], df["Under_prob_odds"] = convert_odds(df['BbAv>2.5'], df['BbAv<2.5'])
    return df


def get_probs(H_xG, A_xG):
    """
    Takes expected goals for home and away team, and calculates
    probabilities for home win, draw and away win by using a poisson
    distribution
    """
    goals_home = []
    goals_away = []
    for i in range(8):
        goals_home.append(poisson.pmf(i, H_xG))
        goals_away.append(poisson.pmf(i, A_xG))
    row = pd.Series(goals_home, index=np.arange(0, 8))
    col = pd.Series(goals_away, index=np.arange(0, 8))
    df = row.apply(lambda r: r * col)
    home = sum(sum(np.tril(df, -1)))
    away = sum(sum(np.triu(df, 1)))
    draw = 1 - home - away
    under = df[0][0] + df[1][0] + df[0][1] + df[2][0] + df[0][2] + df[1][1]
    over = 1 - under
    return np.round(home, 4), np.round(draw, 4), np.round(away, 4), np.round(over, 4), np.round(under, 4)


def rps(prob_h, prob_d, prob_a, home, draw, away):
    """
    Calculates the rank probability score
    prob_h/d/a -> predicted probability
    home/draw/away -> 0 or 1 for actual result
    The lower RPS the better
    """
    step1 = prob_h - home
    step2 = prob_d - draw
    summe = step1 + step2
    rps = (step1 ** 2 + summe ** 2) / 2
    return rps


def get_poi_mas(df):
    df["H_xG_PoiMas"] = (df["H_xG_Poi_mix"] + df["H_xG_Mas"]) / 2
    df["A_xG_PoiMas"] = (df["A_xG_Poi_mix"] + df["A_xG_Mas"]) / 2
    df["H_pred_PoiMas"], df["D_pred_PoiMas"], df["A_pred_PoiMas"], df["O_pred_PoiMas"], df["U_pred_PoiMas"] = get_probs(df["H_xG_PoiMas"], df["A_xG_PoiMas"])
    df["rps_PoiMas"] = rps(df["H_pred_PoiMas"], df["D_pred_PoiMas"], df["A_pred_PoiMas"], df["Home"], df["Draw"], df["Away"])
    return df


def preprocess(df):
    df = make_ints(df)
    df["season"] = int(df.iloc[-1]["Date"][-2:])
    df = get_result_encoding(df)
    df = get_bookie_probs(df)
    df["rps_Book"] = rps(df["H_prob_odds"], df["D_prob_odds"], df["A_prob_odds"], df["Home"],df["Draw"],df["Away"])
    df = get_pl(df)
    df = actual_points(df)
    df = exp_points(df)
    df = actual_ahc(df)
    df = exp_ahc(df)
    return df
