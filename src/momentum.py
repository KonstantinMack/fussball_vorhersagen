
def adj_mom(df, i):
    """
    Creates relative Form from all games (home + away) for the past i games
    relative Form -> sum of points from last i games divided by expected
    points from those games
    """
    df1 = df.loc[:,["HomeTeam", "AwayTeam", "H_Pts", "A_Pts", "H_Pts_Exp", "A_Pts_Exp"]]
    df1.columns = [['Team', 'Team', 'Points', 'Points', "Points_Exp", "Points_Exp"], ['Home', 'Away', 'Home', 'Away', 'Home', 'Away']]
    df1 = df1.stack()
    mom = df1.groupby('Team').Points.apply(lambda x: x.shift().rolling(i).sum())
    mom_exp = df1.groupby('Team').Points_Exp.apply(lambda x: x.shift().rolling(i).sum())
    df1 = df1.assign(Momentum=mom, Momentum_Exp=mom_exp).unstack()
    df1.columns = ["A_Pts", "H_Pts", "A_Pts_Exp", "H_Pts_Exp", "AwayTeam", "HomeTeam", "A_Pts_Tot" + str(i), "H_Pts_Tot" + str(i),"A_Pts_Tot_Exp" + str(i),"H_Pts_Tot_Exp" + str(i)]
    df1 = df1[["HomeTeam", "AwayTeam", "H_Pts_Tot" + str(i), "A_Pts_Tot" + str(i), "H_Pts_Tot_Exp" + str(i), "A_Pts_Tot_Exp" + str(i)]]
    df = df.merge(df1, how="left", on=["HomeTeam", "AwayTeam"])
    df["H_Form_Tot" + str(i)] = df["H_Pts_Tot" + str(i)] / df["H_Pts_Tot_Exp" + str(i)]
    df["A_Form_Tot" + str(i)] = df["A_Pts_Tot" + str(i)] / df["A_Pts_Tot_Exp" + str(i)]
    df["Form_Diff_Tot" + str(i)] = df["H_Form_Tot" + str(i)] - df["A_Form_Tot" + str(i)]
    return df


def last_by(df):
    """
    Calculates Goal Difference + Goal Difference vs handicap for last game
    """
    df1 = df.loc[:,["HomeTeam", "AwayTeam", "GoalDiff", "GoalDiff_Ahc"]]
    df1["GoalDiff_away"] = - df1["GoalDiff"]
    df1["GoalDiff_Ahc_away"] = - df1["GoalDiff_Ahc"]
    df1 = df1[["HomeTeam", "AwayTeam", "GoalDiff", "GoalDiff_away", "GoalDiff_Ahc", "GoalDiff_Ahc_away"]]
    df1.columns = [['Team', 'Team', 'GoalDiff', 'GoalDiff', "GoalDiff_Ahc", "GoalDiff_Ahc"], ['Home', 'Away', 'Home', 'Away', 'Home', 'Away']]
    df1 = df1.stack()
    gd = df1.groupby('Team').GoalDiff.apply(lambda x: x.shift())
    gd_ahc = df1.groupby('Team').GoalDiff_Ahc.apply(lambda x: x.shift())
    df1 = df1.assign(Last_GD=gd, Last_GD_ahc=gd_ahc).unstack()
    df1.columns = ["GoalDiff_Ahc_away", "GoalDiff_Ahc_home", "GoalDiff_away", "GoalDiff_home", "AwayTeam", "HomeTeam", "A_GoalDiff_last", "H_GoalDiff_last", "A_GoalDiff_Ahc_last", "H_GoalDiff_Ahc_last"]
    df1 = df1[["HomeTeam", "AwayTeam", "H_GoalDiff_last", "A_GoalDiff_last", "H_GoalDiff_Ahc_last","A_GoalDiff_Ahc_last"]]
    df = df.merge(df1, how="left", on=["HomeTeam", "AwayTeam"])
    return df


def get_momentum(df, i=4):
    df = adj_mom(df, i)
    df = last_by(df)
    return df
