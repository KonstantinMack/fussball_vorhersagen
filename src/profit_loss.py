
import numpy as np


def home_ahc_pl(df):
    if df["FTHG"] + df["BbAHh"] - df["FTAG"] > 0.25:
        return df["BbAvAHH"] - 1
    elif df["FTHG"] + df["BbAHh"] - df["FTAG"] == 0.25:
        return (df["BbAvAHH"] - 1)/2
    elif df["FTHG"] + df["BbAHh"] - df["FTAG"] == 0:
        return 0
    elif df["FTHG"] + df["BbAHh"] - df["FTAG"] == -0.25:
        return -0.5
    else:
        return -1


def away_ahc_pl(df):
    if df["FTHG"] + df["BbAHh"] - df["FTAG"] > 0.25:
        return -1
    elif df["FTHG"] + df["BbAHh"] - df["FTAG"] == 0.25:
        return -0.5
    elif df["FTHG"] + df["BbAHh"] - df["FTAG"] == 0:
        return 0
    elif df["FTHG"] + df["BbAHh"] - df["FTAG"] == -0.25:
        return (df["BbAvAHA"] - 1) / 2
    else:
        return df["BbAvAHA"] - 1


def get_pl(df):
    df["H_PL"] = np.where(df["FTHG"] > df["FTAG"], df["BbAvH"] - 1, -1)
    df["D_PL"] = np.where(df["FTHG"] == df["FTAG"], df["BbAvD"] - 1, -1)
    df["A_PL"] = np.where(df["FTHG"] < df["FTAG"], df["BbAvA"] - 1, -1)
    df["H_Ahc_PL"] = df.apply(lambda row: home_ahc_pl(row), axis=1)
    df["A_Ahc_PL"] = df.apply(lambda row: away_ahc_pl(row), axis=1)
    df["Over_PL"] = np.where(df["FTHG"] + df["FTAG"] >= 3, df["BbAv>2.5"] - 1, -1)
    df["Under_PL"] = np.where(df["FTHG"] + df["FTAG"] < 3, df["BbAv<2.5"] - 1, -1)
    return df
