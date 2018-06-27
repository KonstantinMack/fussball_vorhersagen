
import numpy as np
import pandas as pd
from sklearn import linear_model
from helper_fcts import get_result_encoding, get_probs, rps


def get_team_encoding(df):
    """
    Creates unique team_Ids for the teams.
    Creates a variable Result which is home_goals - away_goals
    """
    labels, levels = pd.factorize(pd.concat([df["HomeTeam"], df["AwayTeam"]]))
    club_dict = dict(zip(levels, range(len(set(levels)))))
    df["HomeId"] = df["HomeTeam"].map(club_dict)
    df["AwayId"] = df["AwayTeam"].map(club_dict)
    df["Result"] = df["FTHG"] - df["FTAG"]
    df["round"] = df["round"].apply(int)
    return df


def buildGamesMatrix3(games, num_teams):
    """
    Builds match-matrix M that corresponds to each match where the hometeam is
    encoded with +1 and the awayteam with -1.
    Also builds the corresponding results matrix R.
    Inputs: games -> [[Home_Id, Away_Id, HomeGoals, AwayGoals], [],...]
            num_teams -> number of different teams in the league
    """
    l = len(games)
    M = np.zeros([l*2, num_teams*2+1])
    R = np.zeros([l*2])
    for i, j in enumerate(games):
        M[i, j[0]] += 1
        M[i, j[1]+num_teams] += -1
        M[i, num_teams*2] += 1
        M[l+i, j[1]] += 1
        M[l+i, j[0]+num_teams] += -1
        R[i] += j[2]
        R[l+i] += j[3]
    return M, R


def get_ratings(df, num_teams):
    """
    extracts the ratings from M and R by using lin reg
    returns dict for offense ratings, dict for defense ratings, and the
    home-field-advantage HFA
    """
    df2 = df[["HomeId", "AwayId", "FTHG", "FTAG"]]
    M, R = buildGamesMatrix3(df2.values, num_teams)
    clf = linear_model.Ridge(fit_intercept=False, alpha=0.1)
    clf.fit(M,R)
    ratings = clf.coef_
    correction = np.min(ratings[num_teams:2*num_teams])
    ratings[0:2*num_teams] -= correction
    rat_off_dict = dict(zip(range(num_teams),np.round(ratings[:num_teams], 4)))
    rat_def_dict = dict(zip(range(num_teams),np.round(ratings[num_teams:2*num_teams], 4)))
    rat_hfa = np.round(ratings[2*num_teams], 4)
    return rat_off_dict, rat_def_dict, rat_hfa


def get_all_matchday_ratings(df, num_teams):
    """
    calculates the ratings for each matchday
    """
    rat_offense_full = {}
    rat_defense_full = {}
    rat_hfa_full = {}
    for i in range(1, df["round"].max() + 1):
        matchday = df[df["round"] <= i].copy()
        offense, defense, hfa = get_ratings(matchday, num_teams)
        rat_offense_full[i] = offense
        rat_defense_full[i] = defense
        rat_hfa_full[i] = hfa
    return rat_offense_full, rat_defense_full, rat_hfa_full


def get_off_def(df, off_rating, def_rating):
    """
    Creates Dataframes for home_offense, home_defense, away_offense and
    away_defense ratings
    """
    home_off = [df[df["round"] == i+1].HomeId.map(j) for i, j in off_rating.items()]
    home_off = pd.DataFrame(pd.concat(home_off))
    home_off.columns = ["H_Off_Rat"]

    away_off = [df[df["round"] == i+1].AwayId.map(j) for i, j in off_rating.items()]
    away_off = pd.DataFrame(pd.concat(away_off))
    away_off.columns = ["A_Off_Rat"]

    home_def = [df[df["round"] == i+1].HomeId.map(j) for i, j in def_rating.items()]
    home_def = pd.DataFrame(pd.concat(home_def))
    home_def.columns = ["H_Def_Rat"]

    away_def = [df[df["round"] == i+1].AwayId.map(j) for i, j in def_rating.items()]
    away_def = pd.DataFrame(pd.concat(away_def))
    away_def.columns = ["A_Def_Rat"]

    return home_off, away_off, home_def, away_def


def get_exp_goals(df):
    """
    Calculates expected home and away goals from Massey Ratings
    """
    df["H_xG_Mas"] = np.where(df["H_Off_Rat"] - df["A_Def_Rat"] + df["HFA"] > 0, df["H_Off_Rat"] - df["A_Def_Rat"] + df["HFA"], 0)
    df["A_xG_Mas"] = np.where(df["A_Off_Rat"] - df["H_Def_Rat"] > 0, df["A_Off_Rat"] - df["H_Def_Rat"], 0)
    df["xGD_Mas"] = df["H_xG_Mas"] - df["A_xG_Mas"]
    return df


def get_massey(df, num_teams):
    """
    main function: takes Dataframe and returns the Dataframe with ratings
    """
    df = get_result_encoding(df)
    df = get_team_encoding(df)
    rat_off, rat_def, hfa = get_all_matchday_ratings(df, num_teams)
    home_off, away_off, home_def, away_def = get_off_def(df, rat_off, rat_def)
    hfa = pd.DataFrame(pd.Series(hfa), columns=["HFA"]).shift()
    df = df.merge(home_off, left_index=True, right_index=True, how="left")
    df = df.merge(away_off, left_index=True, right_index=True, how="left")
    df = df.merge(home_def, left_index=True, right_index=True, how="left")
    df = df.merge(away_def, left_index=True, right_index=True, how="left")
    df = df.merge(hfa, how="left", left_on="round", right_index=True)
    df = get_exp_goals(df)
    df["H_pred_Mas"], df["D_pred_Mas"], df["A_pred_Mas"] = get_probs(df["H_xG_Mas"], df["A_xG_Mas"])
    df["rps_Mas"] = rps(df["H_pred_Mas"], df["D_pred_Mas"], df["A_pred_Mas"], df["Home"],df["Draw"],df["Away"])
    return df
