
import datetime
import numpy as np
import os
import pandas as pd
import pickle
import requests as re


API = os.getenv('SPORTMONKS')


def get_dates(preds):
    date1 = min(pd.to_datetime(preds.Date, format='%d/%m/%y')).strftime("%Y-%m-%d")
    date2 = max(pd.to_datetime(preds.Date, format='%d/%m/%y')).strftime("%Y-%m-%d")
    return date1, date2


def get_fixtures_bydate(date1, date2):
    url = f"https://soccer.sportmonks.com/api/v2.0/fixtures/between/{date1}/{date2}?api_token={API}&include=localTeam,visitorTeam,league,flatOdds:filter(bookmaker_id|70)"
    fixtures = re.get(url).json()
    pages = fixtures["meta"]["pagination"]["total_pages"]
    if pages > 1:
        fix_list = fixtures["data"]
        for page in range(2,pages+1):
            url2 = url + f"&page={page}"
            next_page = re.get(url2).json()["data"]
            fix_list += next_page
        return fix_list
    return fixtures["data"]


def get_hc_odds(odds_list):
    odds = [x["odds"] for x in odds_list if x["market_id"] == 28]
    if not odds:
        return np.NaN, np.NaN, np.NaN, np.NaN
    df = pd.DataFrame(odds[0])["handicap label value".split()]
    df = df.applymap(float)
    df["diff2"] = (df.value - 1.96)**2
    mini = df.iloc[df.diff2.values.argmin()]
    aprx_hc = mini["handicap"] + (mini["value"] - 1.96) / 1.2
    hc = mini.handicap
    opp = mini.label % 2 + 1
    opp_odds = float(df.loc[(df["handicap"] == -hc) & (df["label"] == opp), "value"])
    if mini.label == 1:
        return hc, round(aprx_hc, 2), mini.value, opp_odds
    else:
        return -hc, round(-aprx_hc, 2), opp_odds, mini.value


def get_relevant_info(fix_list):
    fixtures = []
    for fix in fix_list:
        fix_data = {}
        fix_data["timestamp"] = fix["time"]["starting_at"]["timestamp"]
        fix_data["League_id"] = fix['league']["data"]["id"]
        fix_data["HomeTeam"] = fix['localTeam']['data']['name']
        fix_data["AwayTeam"] = fix['visitorTeam']['data']['name']
        odds = get_hc_odds(fix["flatOdds"].get("data", []))
        fix_data["HC_Pin"] = odds[0]
        fix_data["aprx_HC"] = odds[1]
        fix_data["H_odds"] = odds[2]
        fix_data["A_odds"] = odds[3]
        fixtures.append(fix_data)
    return fixtures


def live_odds(preds):
    date1, date2 = get_dates(preds)
    fixtures = get_fixtures_bydate(date1, date2)
    fixtures = get_relevant_info(fixtures)
    fixtures = pd.DataFrame(fixtures)

    with open('team_dict.pkl', 'rb') as handle:
        team_dict = pickle.load(handle)

    preds["HomeTeam"] = preds.HomeTeam.map(team_dict)
    preds["AwayTeam"] = preds.AwayTeam.map(team_dict)

    fixtures = fixtures.loc[:,["HomeTeam", "AwayTeam", "HC_Pin", "aprx_HC", "H_odds", "A_odds"]]

    merged = preds.merge(fixtures, on=["HomeTeam", "AwayTeam"], how="left")

    merged["Pin_HC_Diff"] = merged.x_HC - merged.aprx_HC
    merged.loc[merged["Pin_HC_Diff"] <= -0.15, "BET_Pin"] = "HOME " + merged["HC_Pin"].apply(str)
    merged.loc[merged["Pin_HC_Diff"] >= 0.15, "BET_Pin"] = "AWAY " + (-merged["HC_Pin"]).apply(str)
    merged.loc[abs(merged["Pin_HC_Diff"]) < 0.15, "BET_Pin"] = "------"

    return merged
