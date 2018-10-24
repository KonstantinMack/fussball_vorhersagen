
from helper_fcts import preprocess, get_poi_mas
from stats2 import get_stats2
from exp_goals_poisson import get_poisson
from massey_ratings_adv import get_massey
from momentum import get_momentum


def modelling(df1, num_teams, stat="MIX", window=6, min_periods=4):
    df = df1.copy()
    df = preprocess(df)
    df = get_momentum(df)
    df = get_stats2(df, window, min_periods)
    df = get_poisson(df, stat)
    df = get_massey(df, num_teams)
    df = get_poi_mas(df)
    return df
