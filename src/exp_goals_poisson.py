
from helper_fcts import get_result_encoding, get_probs, rps


def prepare_data(df):
    """
    Creates necessary variables for expected goals model
    """
    df["LgHG"] = df["FTHG"].expanding().mean().shift()
    df["LgAG"] = df["FTAG"].expanding().mean().shift()
    df["TeamHG"] = df.groupby("HomeTeam")["FTHG"].apply(lambda x: x.expanding().mean().shift())
    df["TeamAG"] = df.groupby("AwayTeam")["FTAG"].apply(lambda x: x.expanding().mean().shift())
    df["Team_c_HG"] = df.groupby("HomeTeam")["FTAG"].apply(lambda x: x.expanding().mean().shift())
    df["Team_c_AG"] = df.groupby("AwayTeam")["FTHG"].apply(lambda x: x.expanding().mean().shift())
    df["H_att_Poi"] = df["TeamHG"] / df["LgHG"]
    df["A_att_Poi"] = df["TeamAG"] / df["LgAG"]
    df["H_def_Poi"] = df["Team_c_HG"] / df["LgAG"]
    df["A_def_Poi"] = df["Team_c_AG"] / df["LgHG"]
    df["H_xG_Poi"] = df["H_att_Poi"] * df["A_def_Poi"] * df["LgHG"]
    df["A_xG_Poi"] = df["A_att_Poi"] * df["H_def_Poi"] * df["LgAG"]
    return df


def get_poisson(df):
    """
    Main function: Takes Dataframe and returns Dataframe with exp goals,
    winning probabilities and RPS of the prediction
    """
    df = get_result_encoding(df)
    df = prepare_data(df)
    df["H_pred_Poi"], df["D_pred_Poi"], df["A_pred_Poi"] = get_probs(df["H_xG_Poi"], df["A_xG_Poi"])
    df["rps_Poi"] = rps(df["H_pred_Poi"], df["D_pred_Poi"], df["A_pred_Poi"], df["Home"],df["Draw"],df["Away"])
    return df
