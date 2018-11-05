
import pandas as pd
from fixtures import get_new_matches
from keras.models import load_model
from sklearn.externals import joblib


def load_scaling(df, league, cols):
    scaler = joblib.load(f'scalers/scaler_{league}.joblib')
    X_scaled = scaler.transform(df[cols].dropna())
    X_unscaled = df[cols].dropna()
    return X_scaled, X_unscaled


def load_clf_models(league):
    rdf_clf = joblib.load(f'model_weights/rdf_clf_{league}.joblib')
    xgb_clf = joblib.load(f'model_weights/xgb_clf_{league}.joblib')

    def loss_rps(y_true, y_pred):
        prob_h = y_pred[:, 0]
        prob_d = y_pred[:, 1]
        home = y_true[:, 0]
        draw = y_true[:, 1]
        step1 = prob_h - home
        step2 = prob_d - draw
        summe = step1 + step2
        return (step1 ** 2 + summe ** 2) / 2

    ann_clf = load_model(f'model_weights/ann_clf_{league}.h5', custom_objects={'loss_rps': loss_rps})

    return rdf_clf, xgb_clf, ann_clf


def load_reg_models(league):
    xgb_reg_h = joblib.load(f'model_weights/xgb_reg_{league}_h.joblib')
    xgb_reg_a = joblib.load(f'model_weights/xgb_reg_{league}_a.joblib')
    svr_reg_h = joblib.load(f'model_weights/svr_reg_{league}_h.joblib')
    svr_reg_a = joblib.load(f'model_weights/svr_reg_{league}_a.joblib')
    ann_reg = load_model('model_weights/ann_reg_eng.h5')
    return xgb_reg_h, xgb_reg_a, svr_reg_h, svr_reg_a, ann_reg


def get_predictions(league):

    league_mapping = {
        "eng": ("E0", 20),
        "eng2": ("E1", 24),
        "eng3": ("E2", 24),
        "fra": ("F1", 20),
        "ita": ("I1", 20),
        "ger": ("D1", 18),
        "spa": ("SP1", 20)
        }

    df = get_new_matches(*league_mapping[league])

    columns_mit_fe = ['H_avgGD', 'A_avgGD', 'H_avgG', 'A_avgG', 'H_avgG_c', 'A_avgG_c', 'H_avgST', 'A_avgST', 'H_avgST_c', 'A_avgST_c', 'H_GoalDiff_last', 'A_GoalDiff_last', 'H_xG_PoiMas', 'A_xG_PoiMas', 'H_Form_Tot4', 'A_Form_Tot4','H_Def_Rat', 'H_Off_Rat', 'A_Def_Rat', 'A_Off_Rat', "H_prob_odds", "D_prob_odds", "A_prob_odds"]
    fixtures = df.loc[df[columns_mit_fe].dropna().index].reset_index(drop=True)

    X_scaled, X_unscaled = load_scaling(fixtures, league, columns_mit_fe)
    rdf_clf, xgb_clf, ann_clf = load_clf_models(league)
    xgb_reg_h, xgb_reg_a, svr_reg_h, svr_reg_a, ann_reg = load_reg_models(league)

    #CLF predictions:
    rdf_pred = rdf_clf.predict_proba(X_unscaled)
    xgb_pred = xgb_clf.predict_proba(X_unscaled)
    ann_clf_pred = ann_clf.predict(X_scaled)

    #REG predictions:
    xgb_reg_pred_h = xgb_reg_h.predict(X_unscaled)
    xgb_reg_pred_a = xgb_reg_a.predict(X_unscaled)
    svr_reg_pred_h = svr_reg_h.predict(X_scaled)
    svr_reg_pred_a = svr_reg_a.predict(X_scaled)
    ann_reg_pred = ann_reg.predict(X_scaled)

    #Create a summary DataFrame:
    rdf_clf_pred = pd.DataFrame(rdf_pred, columns=["A_pred_Rdf", "D_pred_Rdf", "H_pred_Rdf"])
    xgb_clf_pred = pd.DataFrame(xgb_pred, columns=["A_pred_Xgb", "D_pred_Xgb", "H_pred_Xgb"])
    ann_clf_pred = pd.DataFrame(ann_clf_pred, columns=["H_pred_Ann", "D_pred_Ann", "A_pred_Ann"])
    clf_preds = pd.concat([fixtures, rdf_clf_pred, xgb_clf_pred, ann_clf_pred],axis=1)

    clf_preds["H_pred_avg"] = (clf_preds["H_pred_Rdf"] + clf_preds["H_pred_Xgb"] + clf_preds["H_pred_Ann"]) / 3
    clf_preds["D_pred_avg"] = (clf_preds["D_pred_Rdf"] + clf_preds["D_pred_Xgb"] + clf_preds["D_pred_Ann"]) / 3
    clf_preds["A_pred_avg"] = (clf_preds["A_pred_Rdf"] + clf_preds["A_pred_Xgb"] + clf_preds["A_pred_Ann"]) / 3

    clf_preds["H_xgb_xG"] = xgb_reg_pred_h
    clf_preds["A_xgb_xG"] = xgb_reg_pred_a
    clf_preds["XGB_hc"] = clf_preds["A_xgb_xG"] - clf_preds["H_xgb_xG"]
    clf_preds["XGB_Hc_Diff"] = clf_preds["BbAHh"] - clf_preds["XGB_hc"]

    clf_preds["H_svr_xG"] = svr_reg_pred_h
    clf_preds["A_svr_xG"] = svr_reg_pred_a
    clf_preds["SVR_hc"] = clf_preds["A_svr_xG"] - clf_preds["H_svr_xG"]
    clf_preds["SVR_Hc_Diff"] = clf_preds["BbAHh"] - clf_preds["SVR_hc"]

    ann_reg_pred = pd.DataFrame(ann_reg_pred, columns=["H_ann_xG", "A_ann_xG"])
    clf_preds = pd.concat([clf_preds, ann_reg_pred], axis=1)
    clf_preds["ANN_hc"] = clf_preds["A_ann_xG"] - clf_preds["H_ann_xG"]
    clf_preds["ANN_Hc_Diff"] = clf_preds["BbAHh"] - clf_preds["ANN_hc"]

    clf_preds["Hc_avg"] = (clf_preds["ANN_hc"] + clf_preds["XGB_hc"] + clf_preds["SVR_hc"]) / 3
    clf_preds["Hc_Diff_avg"] = (clf_preds["ANN_Hc_Diff"] + clf_preds["XGB_Hc_Diff"] + clf_preds["SVR_Hc_Diff"]) / 3

    all_predictions = clf_preds[["HomeTeam", "AwayTeam", "H_prob_odds", "D_prob_odds", "A_prob_odds", "BbAHh", "H_pred_avg", "D_pred_avg", "A_pred_avg", "Hc_avg", "Hc_Diff_avg", "H_pred_Rdf", "H_pred_Xgb", "H_pred_Ann", "D_pred_Rdf", "D_pred_Xgb", "D_pred_Ann", "A_pred_Rdf", "A_pred_Xgb", "A_pred_Ann", "XGB_hc", "SVR_hc", "ANN_hc"]]

    return all_predictions
