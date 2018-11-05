
def get_avg_goaldiff_rolling(df, window=6, min_periods=4):
    """
    Calculates average goal difference per team at home and away
    """
    home = df.groupby('HomeTeam').GoalDiff.apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift(1))
    away = - df.groupby('AwayTeam').GoalDiff.apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift(1))
    return home, away


def get_avg_goaldiff_expanding(df):
    """
    Calculates average goal difference per team at home and away
    """
    home = df.groupby('HomeTeam').GoalDiff.apply(lambda x: x.expanding().mean().shift(1))
    away = - df.groupby('AwayTeam').GoalDiff.apply(lambda x: x.expanding().mean().shift(1))
    return home, away


def get_avg_goals_rolling(df, window=6, min_periods=4):
    Lg_HG = df["FTHG"].expanding().mean().shift()
    Lg_AG = df["FTAG"].expanding().mean().shift()
    H_avgG = df.groupby("HomeTeam")["FTHG"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    A_avgG = df.groupby("AwayTeam")["FTAG"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    H_avgG_c = df.groupby("HomeTeam")["FTAG"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    A_avgG_c = df.groupby("AwayTeam")["FTHG"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    return Lg_HG, Lg_AG, H_avgG, A_avgG, H_avgG_c, A_avgG_c


def get_avg_goals_expanding(df):
    Lg_HG = df["FTHG"].expanding().mean().shift()
    Lg_AG = df["FTAG"].expanding().mean().shift()
    H_avgG = df.groupby("HomeTeam")["FTHG"].apply(lambda x: x.expanding().mean().shift())
    A_avgG = df.groupby("AwayTeam")["FTAG"].apply(lambda x: x.expanding().mean().shift())
    H_avgG_c = df.groupby("HomeTeam")["FTAG"].apply(lambda x: x.expanding().mean().shift())
    A_avgG_c = df.groupby("AwayTeam")["FTHG"].apply(lambda x: x.expanding().mean().shift())
    return Lg_HG, Lg_AG, H_avgG, A_avgG, H_avgG_c, A_avgG_c


def get_avg_shots_rolling(df, window=6, min_periods=4):
    Lg_HS = df["HS"].expanding().mean().shift()
    Lg_AS = df["AS"].expanding().mean().shift()
    Lg_HST = df["HST"].expanding().mean().shift()
    Lg_AST = df["AST"].expanding().mean().shift()
    H_avgS = df.groupby("HomeTeam")["HS"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    A_avgS = df.groupby("AwayTeam")["AS"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    H_avgS_c = df.groupby("HomeTeam")["AS"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    A_avgS_c = df.groupby("AwayTeam")["HS"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    H_avgST = df.groupby("HomeTeam")["HST"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    A_avgST = df.groupby("AwayTeam")["AST"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    H_avgST_c = df.groupby("HomeTeam")["AST"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    A_avgST_c = df.groupby("AwayTeam")["HST"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    return Lg_HS, Lg_AS, Lg_HST, Lg_AST, H_avgS, A_avgS, H_avgS_c, A_avgS_c, H_avgST, A_avgST, H_avgST_c, A_avgST_c


def get_avg_shots_expanding(df):
    Lg_HS = df["HS"].expanding().mean().shift()
    Lg_AS = df["AS"].expanding().mean().shift()
    Lg_HST = df["HST"].expanding().mean().shift()
    Lg_AST = df["AST"].expanding().mean().shift()
    H_avgS = df.groupby("HomeTeam")["HS"].apply(lambda x: x.expanding().mean().shift())
    A_avgS = df.groupby("AwayTeam")["AS"].apply(lambda x: x.expanding().mean().shift())
    H_avgS_c = df.groupby("HomeTeam")["AS"].apply(lambda x: x.expanding().mean().shift())
    A_avgS_c = df.groupby("AwayTeam")["HS"].apply(lambda x: x.expanding().mean().shift())
    H_avgST = df.groupby("HomeTeam")["HST"].apply(lambda x: x.expanding().mean().shift())
    A_avgST = df.groupby("AwayTeam")["AST"].apply(lambda x: x.expanding().mean().shift())
    H_avgST_c = df.groupby("HomeTeam")["AST"].apply(lambda x: x.expanding().mean().shift())
    A_avgST_c = df.groupby("AwayTeam")["HST"].apply(lambda x: x.expanding().mean().shift())
    return Lg_HS, Lg_AS, Lg_HST, Lg_AST, H_avgS, A_avgS, H_avgS_c, A_avgS_c, H_avgST, A_avgST, H_avgST_c, A_avgST_c


def get_avg_corners_rolling(df, window=6, min_periods=4):
    H_avgC = df.groupby("HomeTeam")["HC"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    A_avgC = df.groupby("AwayTeam")["AC"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    H_avgC_c = df.groupby("HomeTeam")["AC"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    A_avgC_c = df.groupby("AwayTeam")["HC"].apply(lambda x: x.rolling(window=window, min_periods=min_periods).mean().shift())
    return H_avgC, A_avgC, H_avgC_c, A_avgC_c


def get_avg_corners_expanding(df):
    H_avgC = df.groupby("HomeTeam")["HC"].apply(lambda x: x.expanding().mean().shift())
    A_avgC = df.groupby("AwayTeam")["AC"].apply(lambda x: x.expanding().mean().shift())
    H_avgC_c = df.groupby("HomeTeam")["AC"].apply(lambda x: x.expanding().mean().shift())
    A_avgC_c = df.groupby("AwayTeam")["HC"].apply(lambda x: x.expanding().mean().shift())
    return H_avgC, A_avgC, H_avgC_c, A_avgC_c


def get_stats(df2, mode="expanding", window=6, min_periods=4):
    df = df2.copy()
    if mode == "rolling":
        df["H_avgGD"], df["A_avgGD"] = get_avg_goaldiff_rolling(df, window, min_periods)
        df["Lg_HG"], df["Lg_AG"], df["H_avgG"], df["A_avgG"], df["H_avgG_c"], df["A_avgG_c"] = get_avg_goals_rolling(df, window, min_periods)
        df["Lg_HS"], df["Lg_AS"], df["Lg_HST"], df["Lg_AST"], df["H_avgS"], df["A_avgS"], df["H_avgS_c"], df["A_avgS_c"], df["H_avgST"], df["A_avgST"], df["H_avgST_c"], df["A_avgST_c"] = get_avg_shots_rolling(df, window, min_periods)
    else:
        df["H_avgGD"], df["A_avgGD"] = get_avg_goaldiff_expanding(df)
        df["Lg_HG"], df["Lg_AG"], df["H_avgG"], df["A_avgG"], df["H_avgG_c"], df["A_avgG_c"] = get_avg_goals_expanding(df)
        df["Lg_HS"], df["Lg_AS"], df["Lg_HST"], df["Lg_AST"], df["H_avgS"], df["A_avgS"], df["H_avgS_c"], df["A_avgS_c"], df["H_avgST"], df["A_avgST"], df["H_avgST_c"], df["A_avgST_c"] = get_avg_shots_expanding(df)
    return df


def get_stats2(df2, window=6, min_periods=4):
    df = df2.copy()
    H_avgGDr, A_avgGDr = get_avg_goaldiff_rolling(df, window, min_periods)
    H_avgGDe, A_avgGDe = get_avg_goaldiff_expanding(df)
    df["H_avgGD"] = (H_avgGDr + 2 * H_avgGDe) / 3
    df["A_avgGD"] = (A_avgGDr + 2 * A_avgGDe) / 3

    Lg_HG, Lg_AG, H_avgG, A_avgG, H_avgG_c, A_avgG_c = get_avg_goals_rolling(df, window, min_periods)
    Lg_HGe, Lg_AGe, H_avgGe, A_avgGe, H_avgG_ce, A_avgG_ce = get_avg_goals_expanding(df)
    df["Lg_HG"] = (Lg_HG + 2*Lg_HGe) / 3
    df["Lg_AG"] = (Lg_AG + 2*Lg_AGe) / 3
    df["H_avgG"] = (H_avgG + 2*H_avgGe) / 3
    df["A_avgG"] = (A_avgG + 2*A_avgGe) / 3
    df["H_avgG_c"] = (H_avgG_c + 2*H_avgG_ce) / 3
    df["A_avgG_c"] = (A_avgG_c + 2*A_avgG_ce) / 3

    Lg_HS, Lg_AS, Lg_HST, Lg_AST, H_avgS, A_avgS, H_avgS_c, A_avgS_c, H_avgST, A_avgST, H_avgST_c, A_avgST_c = get_avg_shots_rolling(df, window, min_periods)
    Lg_HSe, Lg_ASe, Lg_HSTe, Lg_ASTe, H_avgSe, A_avgSe, H_avgS_ce, A_avgS_ce, H_avgSTe, A_avgSTe, H_avgST_ce, A_avgST_ce = get_avg_shots_expanding(df)

    H_avgC, A_avgC, H_avgC_c, A_avgC_c = get_avg_corners_rolling(df, window, min_periods)
    H_avgCe, A_avgCe, H_avgC_ce, A_avgC_ce = get_avg_corners_expanding(df)

    df["Lg_HS"] = (Lg_HS + 2*Lg_HSe) / 3
    df["Lg_AS"] = (Lg_AS + 2*Lg_ASe) / 3
    df["Lg_HST"] = (Lg_HST + 2*Lg_HSTe) / 3
    df["Lg_AST"] = (Lg_AST + 2*Lg_ASTe) / 3
    df["H_avgS"] = (H_avgS + 2*H_avgSe) / 3
    df["A_avgS"] = (A_avgS + 2*A_avgSe) / 3
    df["H_avgS_c"] = (H_avgS_c + 2*H_avgS_ce) / 3
    df["A_avgS_c"] = (A_avgS_c + 2*A_avgS_ce) / 3
    df["H_avgST"] = (H_avgST + 2*H_avgSTe) / 3
    df["A_avgST"] = (A_avgST + 2*A_avgSTe) / 3
    df["H_avgST_c"] = (H_avgST_c + 2*H_avgST_ce) / 3
    df["A_avgST_c"] = (A_avgST_c + 2*A_avgST_ce) / 3

    df["H_avgC"] = (H_avgC + 2*H_avgCe) / 3
    df["A_avgC"] = (A_avgC + 2*A_avgCe) / 3
    df["H_avgC_c"] = (H_avgC_c + 2*H_avgC_ce) / 3
    df["A_avgC_c"] = (A_avgC_c + 2*A_avgC_ce) / 3

    return df
