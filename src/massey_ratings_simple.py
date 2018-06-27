
import numpy as np
import pandas as pd


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


def buildGamesMatrix(games, num_teams):
    """
    Builds match-matrix M that corresponds to each match where the hometeam is
    encoded with +1 and the awayteam with -1.
    Also builds the corresponding results matrix R.
    Inputs: games -> [[Home_Id, Away_Id, Result], [],...]
            num_teams -> number of different teams in the league
    """
    M = np.zeros([len(games), num_teams])
    R = np.zeros([len(games)])
    for idx, g in enumerate(games):
        M[idx, g[0]] = 1
        M[idx, g[1]] = -1
        R[idx] = g[2]
    M = np.vstack((M, [1]*num_teams))
    R = np.append(R, 0)
    return M, R


def get_ratings(df, num_teams):
    """
    extracts the ratings from M and R by using lin reg
    """
    df2 = df[["HomeId", "AwayId", "Result"]]
    M, R = buildGamesMatrix(df2.values, num_teams)
    ratings = np.linalg.lstsq(M,R)[0]
    ratings_dict = dict(zip(range(num_teams),np.round(ratings, 4)))
    return ratings_dict


def get_all_matchday_ratings(df, num_teams):
    """
    calculates the ratings for each matchday
    """
    ratings_full = {}
    for i in range(1, df["round"].max() + 1):
        matchday = df[df["round"] <= i].copy()
        ratings = get_ratings(matchday, num_teams)
        ratings_full[i] = ratings
    return ratings_full


def get_massey(df, num_teams):
    """
    main file: takes Dataframe and returns the Dataframe with ratings
    """
    df = get_team_encoding(df)
    ratings_full = get_all_matchday_ratings(df, num_teams)
    home = [df[df["round"] == i+1].HomeId.map(j) for i, j in ratings_full.items()]
    away = [df[df["round"] == i+1].AwayId.map(j) for i, j in ratings_full.items()]
    home_rat = pd.DataFrame(pd.concat(home))
    home_rat.columns = ["HomeRat"]
    away_rat = pd.DataFrame(pd.concat(away))
    away_rat.columns = ["AwayRat"]
    df = df.merge(home_rat, left_index=True, right_index=True, how="left")
    df = df.merge(away_rat, left_index=True, right_index=True, how="left")
    return df
