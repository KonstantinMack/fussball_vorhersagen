
import datetime
import pandas as pd
import xgboost as xgb

from keras.models import load_model
from sklearn.externals import joblib

from fixtures import get_fixtures, get_fixtures_other
from fixtures_sportmonks import get_fixtures_sportsmonks, get_fixtures_other_sportsmonks


PATH = "C:\\Users\\Konny\\DataScience\\SpicedAcademy\\fussball_vorhersagen\\src\\"
DATE = datetime.datetime.now().strftime("%d-%m-%y")
COLS = ['H_avgGD', 'A_avgGD', 'H_avgG', 'A_avgG', 'H_avgG_c', 'A_avgG_c', 'H_avgST', 'A_avgST', 'H_avgST_c', 'A_avgST_c', 'H_avgC', 'A_avgC', 'H_avgC_c', 'A_avgC_c', 'H_GoalDiff_last', 'A_GoalDiff_last', 'H_xG_PoiMas', 'A_xG_PoiMas', 'H_Form_Tot4', 'A_Form_Tot4','H_Def_Rat', 'H_Off_Rat', 'A_Def_Rat', 'A_Off_Rat', "H_prob_odds", "D_prob_odds", "A_prob_odds", "D1", "E0", "E1", "E2", "E3", "F1", "I1", "SP1"]


def approx_goaldiff(line, ahc_home_odds):
    """
    Approximates goal difference suggested by bookmaker's line and odds
    """
    diff = (ahc_home_odds - 1.93) / 1.25
    return round(line + diff, 2)


def get_models(df, X, prefix=""):
    """
    Loads and runs the different models and returns their predictions
    """

    ### XGB
    xgb_h = joblib.load(PATH + "model_weights\\{}xgb_h.model".format(prefix))
    xgb_a = joblib.load(PATH + "model_weights\\{}xgb_a.model".format(prefix))
    DMtrain = xgb.DMatrix(data=X)
    xgb_hg = xgb_h.predict(DMtrain)
    xgb_ag = xgb_a.predict(DMtrain)

    ### Lin Reg
    lin_reg_h = joblib.load(PATH + "model_weights\\{}lin_reg_h.joblib".format(prefix))
    lin_reg_a = joblib.load(PATH + "model_weights\\{}lin_reg_a.joblib".format(prefix))
    lin_hg = lin_reg_h.predict(X)
    lin_ag = lin_reg_a.predict(X)

    ### ANN
    model = load_model(PATH + "model_weights\\{}ann_reg.h5".format(prefix))
    scaler_x = joblib.load(PATH + "model_weights\\{}ann_scaler_x.joblib".format(prefix))
    X_scaled = scaler_x.transform(X)
    ann = model.predict(X_scaled)
    scaler_y = joblib.load(PATH + "model_weights\\{}ann_scaler_y.joblib".format(prefix))
    ann_preds = scaler_y.inverse_transform(ann)
    ann_preds = pd.DataFrame(ann_preds, columns=["ANN_HG", "ANN_AG"])

    ### putting the results together
    df["adj_AHC"] = approx_goaldiff(df.BbAHh, df.BbAvAHH)

    df["XGB_HG"] = xgb_hg
    df["XGB_AG"] = xgb_ag
    df["XGB_HC_Diff"] = df["XGB_AG"] - df["XGB_HG"] - df["adj_AHC"]

    df["LIN_HG"] = lin_hg
    df["LIN_AG"] = lin_ag
    df["LIN_HC_Diff"] = df["LIN_AG"] - df["LIN_HG"] - df["adj_AHC"]

    df = pd.concat([df, ann_preds], axis=1)
    df["ANN_HC_Diff"] = df["ANN_AG"] - df["ANN_HG"] - df["adj_AHC"]

    df["Diff"] = round((df["ANN_HC_Diff"] + df["XGB_HC_Diff"] + df["LIN_HC_Diff"]) / 3, 2)

    df["x_HG"] = (df["XGB_HG"] + df["LIN_HG"] + df["ANN_HG"]) / 3
    df["x_AG"] = (df["XGB_AG"] + df["LIN_AG"] + df["ANN_AG"]) / 3
    df["x_HC"] = df["x_AG"] - df["x_HG"]

    df["AHC"] = df["BbAHh"]
    df = df.round({"x_HG": 2, "x_AG": 2, "x_HC": 2, "HC_Diff_Avg":2})

    return df


def get_predictions(save=None):
    """
    Calculates predictions for the new matchday
    save: if save -> saves predictions as pickle file
    """
    new_matches = pd.read_csv("http://www.football-data.co.uk/fixtures.csv")
    fix_date = max(pd.to_datetime(new_matches.Date, format='%d/%m/%y'))
    if datetime.date.today() > fix_date.date():
        print("No new matches! Come back later!\nData for new matches usually arrives Tuesday for midweek matches and friday for weekend matches.")
        preds = None
        bets = None

    else:
        print("preprocessing major leagues...")

        main_leagues = get_fixtures()
        if main_leagues.empty:
            print("no major leagues this matchday")
        else:
            X_main = main_leagues[COLS]
            df_main = get_models(main_leagues, X_main)

        print("preprocessing minor leagues...")

        other_leagues = get_fixtures_other()
        if other_leagues.empty:
            print("no minor leagues this matchday")
        else:
            X_other = other_leagues[COLS[:-8]]
            df_other = get_models(other_leagues, X_other, "other_")

        print("evaluating models...")
        if not main_leagues.empty and not other_leagues.empty:
            df = pd.concat([df_main, df_other]).reset_index(drop=True)
        elif not main_leagues.empty and other_leagues.empty:
            df = df_main.copy()
        elif not other_leagues.empty and main_leagues.empty:
            df = df_other.copy()
        else:
            print("There are no matches on this week")
            return None, None

        df.loc[df["Diff"] <= -0.15, "BET"] = "HOME " + df["AHC"].apply(str)
        df.loc[df["Diff"] >= 0.15, "BET"] = "AWAY " + (-df["AHC"]).apply(str)
        df.loc[abs(df["Diff"]) < 0.15, "BET"] = "------"

        preds = df.loc[:,["Date", "Div", "HomeTeam", "AwayTeam", "x_HG", "x_AG", "x_HC", "AHC", "adj_AHC", "Diff", "BbAvAHH", "BbAvAHA", "BET"]]
        preds = preds.rename({"BbAvAHH": "H_Odds", "BbAvAHA": "A_Odds"}, axis="columns")

        bets = preds.loc[abs(preds["Diff"]) >= 0.15].reset_index(drop=True)

        if save:
            preds.to_pickle(PATH + f"predictions\\pkl\\prediction_{DATE}.pkl")
            preds.to_excel(PATH + f"predictions\\excel\\prediction_{DATE}.xlsx")
        print("Done! Good luck!")
    return preds, bets


def get_predictions_sportmonks(date1, date2, save=None):
    """
    Calculates predictions for the new matchday
    save: if save -> saves predictions as pickle file
    date format: "2018-11-16"
    """
    print("preprocessing major leagues...")

    main_leagues = get_fixtures_sportsmonks(date1, date2)
    if main_leagues.empty:
        print("no major leagues this matchday")
    else:
        X_main = main_leagues[COLS]
        df_main = get_models(main_leagues, X_main)

    print("preprocessing minor leagues...")

    other_leagues = get_fixtures_other_sportsmonks(date1, date2)
    if other_leagues.empty:
        print("no minor leagues this matchday")
    else:
        X_other = other_leagues[COLS[:-8]]
        df_other = get_models(other_leagues, X_other, "other_")

    print("evaluating models...")
    if not main_leagues.empty and not other_leagues.empty:
        df = pd.concat([df_main, df_other]).reset_index(drop=True)
    elif not main_leagues.empty and other_leagues.empty:
        df = df_main.copy()
    elif not other_leagues.empty and main_leagues.empty:
        df = df_other.copy()
    else:
        print("There are no matches on this week")
        return None, None

    df.loc[df["Diff"] <= -0.15, "BET"] = "HOME " + df["AHC"].apply(str)
    df.loc[df["Diff"] >= 0.15, "BET"] = "AWAY " + (-df["AHC"]).apply(str)
    df.loc[abs(df["Diff"]) < 0.15, "BET"] = "------"

    preds = df.loc[:,["Date", "Div", "HomeTeam", "AwayTeam", "x_HG", "x_AG", "x_HC", "AHC", "adj_AHC", "Diff", "BbAvAHH", "BbAvAHA", "BET"]]
    preds = preds.rename({"BbAvAHH": "H_Odds", "BbAvAHA": "A_Odds"}, axis="columns")

    bets = preds.loc[abs(preds["Diff"]) >= 0.15].reset_index(drop=True)

    if save:
        preds.to_pickle(PATH + f"predictions\\pkl\\prediction_{DATE}.pkl")
        preds.to_excel(PATH + f"predictions\\excel\\prediction_{DATE}.xlsx")
    print("Done! Good luck!")
    return preds, bets
