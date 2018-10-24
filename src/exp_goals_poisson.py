
from helper_fcts import get_probs, rps


def prepare_poisson(df, stat):
    """
    Creates necessary variables for expected goals model
    """
    df["H_att_Poi" + stat] = df["H_avg" + stat] / df["Lg_H" + stat]
    df["A_att_Poi" + stat] = df["A_avg" + stat] / df["Lg_A" + stat]
    df["H_def_Poi" + stat] = df["H_avg" + stat + "_c"] / df["Lg_A" + stat]
    df["A_def_Poi" + stat] = df["A_avg" + stat + "_c"] / df["Lg_H" + stat]
    df["H_xG_Poi" + stat] = df["H_att_Poi" + stat] * df["A_def_Poi" + stat] * df["Lg_HG"]
    df["A_xG_Poi" + stat] = df["A_att_Poi" + stat] * df["H_def_Poi" + stat] * df["Lg_AG"]
    return df


def shot_mix(df1):
    """
    Calculates the average of the poisson models for shots and shots on target
    """
    df1["H_att_Poi_mix"] = (3*df1["H_att_PoiS"] + 3*df1["H_att_PoiST"] + 2*df1["H_att_PoiG"]) / 8
    df1["A_att_Poi_mix"] = (3*df1["A_att_PoiS"] + 3*df1["A_att_PoiST"] + 2*df1["A_att_PoiG"]) / 8
    df1["H_def_Poi_mix"] = (3*df1["H_def_PoiS"] + 3*df1["H_def_PoiST"] + 2*df1["H_def_PoiG"]) / 8
    df1["A_def_Poi_mix"] = (3*df1["A_def_PoiS"] + 3*df1["A_def_PoiST"] + 2*df1["A_def_PoiG"]) / 8
    # df1["H_att_Poi_mix"] = (df1["H_att_PoiS"] + df1["H_att_PoiST"]) / 2
    # df1["A_att_Poi_mix"] = (df1["A_att_PoiS"] + df1["A_att_PoiST"]) / 2
    # df1["H_def_Poi_mix"] = (df1["H_def_PoiS"] + df1["H_def_PoiST"]) / 2
    # df1["A_def_Poi_mix"] = (df1["A_def_PoiS"] + df1["A_def_PoiST"]) / 2
    df1["H_xG_Poi_mix"] = df1["H_att_Poi_mix"] * df1["A_def_Poi_mix"] * df1["Lg_HG"]
    df1["A_xG_Poi_mix"] = df1["A_att_Poi_mix"] * df1["H_def_Poi_mix"] * df1["Lg_AG"]
    df1["H_pred_Poi_mix"], df1["D_pred_Poi_mix"], df1["A_pred_Poi_mix"], df1["O_pred_Poi_mix"], df1["U_pred_Poi_mix"] = get_probs(df1["H_xG_Poi_mix"], df1["A_xG_Poi_mix"])
    df1["rps_Poi_mix"] = rps(df1["H_pred_Poi_mix"], df1["D_pred_Poi_mix"], df1["A_pred_Poi_mix"], df1["Home"], df1["Draw"], df1["Away"])
    return df1


def delete_stats(df):
    """
    Gets rid of unwanted columns
    """
    del df["H_att_PoiS"]
    del df["H_att_PoiST"]
    del df["H_att_PoiG"]
    del df["A_att_PoiS"]
    del df["A_att_PoiST"]
    del df["A_att_PoiG"]
    del df["H_def_PoiS"]
    del df["H_def_PoiST"]
    del df["H_def_PoiG"]
    del df["A_def_PoiS"]
    del df["A_def_PoiST"]
    del df["A_def_PoiG"]
    del df["H_xG_PoiS"]
    del df["H_xG_PoiST"]
    del df["H_xG_PoiG"]
    del df["A_xG_PoiS"]
    del df["A_xG_PoiST"]
    del df["A_xG_PoiG"]
    return df


def get_poisson(df, stat="MIX"):
    """
    Main function: Takes Dataframe and returns Dataframe with exp goals,
    winning probabilities and RPS of the prediction
    stat: the statistic that is used to calculate the poisson model
        G(oals), S(hots), ST(arget), MIX between them
    delete:
    """
    assert stat in ["G", "S", "ST", "MIX", "ALL"], "Choose G, S, ST, MIX or ALL as stat"

    if stat == "MIX":
        df1 = df.copy()
        for i in ["G", "S", "ST"]:
            df1 = prepare_poisson(df1, i)
        df1 = shot_mix(df1)
        df1 = delete_stats(df1)
        return df1

    elif stat == "ALL":
        df1 = df.copy()
        for i in ["G", "S", "ST"]:
            df1 = prepare_poisson(df1, i)
            df1["H_pred_Poi" + i], df1["D_pred_Poi" + i], df1["A_pred_Poi" + i], df1["O_pred_Poi" + i], df1["U_pred_Poi" + i] = get_probs(df1["H_xG_Poi" + i], df1["A_xG_Poi" + i])
            df1["rps_Poi" + i] = rps(df1["H_pred_Poi" + i], df1["D_pred_Poi" + i], df1["A_pred_Poi" + i], df1["Home"], df1["Draw"], df1["Away"])
        df1 = shot_mix(df1)
        return df1

    else:
        df1 = df.copy()
        df1 = prepare_poisson(df1, stat)
        df1["H_pred_Poi" + stat], df1["D_pred_Poi" + stat], df1["A_pred_Poi" + stat], df1["O_pred_Poi" + stat], df1["U_pred_Poi" + stat] = get_probs(df1["H_xG_Poi" + stat], df1["A_xG_Poi" + stat])
        df1["rps_Poi" + stat] = rps(df1["H_pred_Poi" + stat], df1["D_pred_Poi" + stat], df1["A_pred_Poi" + stat], df1["Home"], df1["Draw"], df1["Away"])
        return df1
