
def get_avg_goaldiff(df):
    """
    Calculates average goal difference per team at home and away
    """
    df["H_avg_GoalDiff"] = df.groupby('HomeTeam').GoalDiff.apply(lambda x: x.expanding().mean().shift(1))
    df["A_avg_GoalDiff"] = - df.groupby('AwayTeam').GoalDiff.apply(lambda x: x.expanding().mean().shift(1))
    return df


def get_avg_goals(df):
    df["LgHG"] = df["FTHG"].expanding().mean().shift()
    df["LgAG"] = df["FTAG"].expanding().mean().shift()
    df["H_avgG"] = df.groupby("HomeTeam")["FTHG"].apply(lambda x: x.expanding().mean().shift())
    df["A_avgG"] = df.groupby("AwayTeam")["FTAG"].apply(lambda x: x.expanding().mean().shift())
    df["H_avgG_c"] = df.groupby("HomeTeam")["FTAG"].apply(lambda x: x.expanding().mean().shift())
    df["A_avgG_c"] = df.groupby("AwayTeam")["FTHG"].apply(lambda x: x.expanding().mean().shift())
    return df


def get_avg_shots(df):
    df["LgHS"] = df["HS"].expanding().mean().shift()
    df["LgAS"] = df["AS"].expanding().mean().shift()
    df["LgHST"] = df["HST"].expanding().mean().shift()
    df["LgAST"] = df["AST"].expanding().mean().shift()
    df["H_avgS"] = df.groupby("HomeTeam")["HS"].apply(lambda x: x.expanding().mean().shift())
    df["A_avgS"] = df.groupby("AwayTeam")["AS"].apply(lambda x: x.expanding().mean().shift())
    df["H_avgS_c"] = df.groupby("HomeTeam")["AS"].apply(lambda x: x.expanding().mean().shift())
    df["A_avgS_c"] = df.groupby("AwayTeam")["HS"].apply(lambda x: x.expanding().mean().shift())
    df["H_avgST"] = df.groupby("HomeTeam")["HST"].apply(lambda x: x.expanding().mean().shift())
    df["A_avgST"] = df.groupby("AwayTeam")["AST"].apply(lambda x: x.expanding().mean().shift())
    df["H_avgST_c"] = df.groupby("HomeTeam")["AST"].apply(lambda x: x.expanding().mean().shift())
    df["A_avgST_c"] = df.groupby("AwayTeam")["HST"].apply(lambda x: x.expanding().mean().shift())
    return df


def get_stats(df):
    df = get_avg_goaldiff(df)
    df = get_avg_goals(df)
    df = get_avg_shots(df)
    return df
