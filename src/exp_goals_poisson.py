
from helper_fcts import get_probs, rps


def prepare_poisson(df, stat):
    """
    Creates necessary variables for expected goals model
    """
    df["H_att_Poi"] = df["H_avg" + stat] / df["LgH" + stat]
    df["A_att_Poi"] = df["A_avg" + stat] / df["LgA" + stat]
    df["H_def_Poi"] = df["H_avg" + stat + "_c"] / df["LgA" + stat]
    df["A_def_Poi"] = df["A_avg" + stat + "_c"] / df["LgH" + stat]
    df["H_xG_Poi"] = df["H_att_Poi"] * df["A_def_Poi"] * df["LgHG"]
    df["A_xG_Poi"] = df["A_att_Poi"] * df["H_def_Poi"] * df["LgAG"]
    return df


def get_poisson(df, stat="G"):
    """
    Main function: Takes Dataframe and returns Dataframe with exp goals,
    winning probabilities and RPS of the prediction
    """
    assert stat in ["G", "S", "ST"], "Choose G, S or ST as stat"

    df = prepare_poisson(df, stat)
    df["H_pred_Poi" + stat], df["D_pred_Poi" + stat], df["A_pred_Poi" + stat] = get_probs(df["H_xG_Poi"], df["A_xG_Poi"])
    df["rps_Poi" + stat] = rps(df["H_pred_Poi" + stat], df["D_pred_Poi" + stat], df["A_pred_Poi" + stat], df["Home"],df["Draw"],df["Away"])
    return df
