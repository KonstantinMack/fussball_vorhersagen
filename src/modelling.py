
import exp_goals_poisson
import helper_fcts
import massey_ratings_adv
import momentum
import stats2


def modelling(df1, num_teams, stat="MIX", window=6, min_periods=4):
    df = df1.copy()
    df = helper_fcts.preprocess(df)
    df = momentum.get_momentum(df)
    df = stats2.get_stats2(df, window, min_periods)
    df = exp_goals_poisson.get_poisson(df, stat)
    df = massey_ratings_adv.get_massey(df, num_teams)
    df = helper_fcts.get_poi_mas(df)
    return df
