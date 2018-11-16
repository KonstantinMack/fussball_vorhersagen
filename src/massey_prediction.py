
import numpy as np
import pandas as pd
from sklearn import linear_model


def get_round(df, num_teams):
    matches = int(num_teams / 2)
    matchday_list = sum([[i] * matches for i in range(1, 50)], [])
    df["round"] = matchday_list[:df.shape[0]]
    return df


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
    return df, club_dict


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


def get_ratings(df, num_teams, club_dict):
    """
    extracts the ratings from M and R by using lin reg
    returns dict for offense ratings, dict for defense ratings, and the
    home-field-advantage HFA
    """
    df2 = df[["HomeId", "AwayId", "FTHG", "FTAG"]].applymap(int)
    M, R = buildGamesMatrix3(df2.values, num_teams)
    clf = linear_model.Ridge(fit_intercept=False, alpha=0.1)
    clf.fit(M,R)
    ratings = clf.coef_
    correction = np.min(ratings[num_teams:2*num_teams])
    ratings[0:2*num_teams] -= correction
    rat_off_dict = dict(zip(range(num_teams),np.round(ratings[:num_teams], 4)))
    rat_def_dict = dict(zip(range(num_teams),np.round(ratings[num_teams:2*num_teams], 4)))
    rat_hfa = np.round(ratings[2*num_teams], 4)
    rat_off = {club: rat_off_dict[idx] for club, idx in club_dict.items()}
    rat_def = {club: rat_def_dict[idx] for club, idx in club_dict.items()}
    return rat_off, rat_def, rat_hfa


def massey_prediction_main(df, num_teams):
    """
    Main function to get Massey Ratings for new fixtures
    """
    df = get_round(df, num_teams)
    df, club_dict = get_team_encoding(df)
    rat_off, rat_def, rat_hfa = get_ratings(df, num_teams, club_dict)
    return rat_off, rat_def, rat_hfa
