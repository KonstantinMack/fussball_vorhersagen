
import pandas as pd
import numpy as np
from scipy.stats import poisson


def get_result_encoding(df):
    """
    Creates an encoding for the result
    """
    df["Home"] = np.where(df["FTHG"] > df["FTAG"], 1, 0)
    df["Draw"] = np.where(df["FTHG"] == df["FTAG"], 1, 0)
    df["Away"] = np.where(df["FTHG"] < df["FTAG"], 1, 0)
    return df


def convert_odds(odds_h, odds_d, odds_a):
    """
    Converts odds to probabilities
    """
    inv_h = 1 / odds_h
    inv_d = 1 / odds_d
    inv_a = 1 / odds_a
    inv_sum = inv_h + inv_d + inv_a
    return inv_h / inv_sum, inv_d / inv_sum, inv_a / inv_sum


def get_bookie_probs(df):
    """
    Calculates the outcome probabilities which are implied by the
    bookmaker's odds
    """
    df["H_prob_odds"], df["D_prob_odds"], df["A_prob_odds"] = convert_odds(df["PSCH"], df["PSCD"], df["PSCA"])
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
    return np.round(home, 4), np.round(draw, 4), np.round(away, 4)


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
