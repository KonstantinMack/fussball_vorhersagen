### Deprecated


import os
import requests
import pandas as pd


REFRESH_TOKEN = os.getenv('SPORTDEER')
access_token = requests.get("https://api.sportdeer.com/v1/accessToken?refresh_token=" + REFRESH_TOKEN).json()["new_access_token"]


def get_content_pages(url):
    """
    extracts number of pages for paginated API responses
    """
    site = requests.get(url).json()
    content = site["docs"]
    pages = site["pagination"]["pages"]
    return content, pages


def get_all_countries():
    url = f"https://api.sportdeer.com/v1/countries?access_token={access_token}"
    countries = requests.get(url).json()["docs"]
    countries = [(i['name'], i['_id']) for i in countries]
    return countries


def get_all_seasons():
    url = f"https://api.sportdeer.com/v1/seasons?access_token={access_token}"
    content, pages = get_content_pages(url)
    seasons = []
    for i in range(1, pages + 1):
        url = f"https://api.sportdeer.com/v1/seasons?page={str(i)}&access_token={access_token}"
        seasons += requests.get(url).json()["docs"]
    seasons = [(i['name'], i['_id']) for i in seasons]
    return seasons


def get_lineup(fix_id):
    url = f"https://api.sportdeer.com/v1/fixtures/{fix_id}/lineups?access_token={access_token}"
    content, pages = get_content_pages(url)
    lineup = []
    for i in range(1, pages + 1):
        url = f"https://api.sportdeer.com/v1/fixtures/{fix_id}/lineups?page={str(i)}&access_token={access_token}"
        lineup += [i for i in requests.get(url).json()["docs"] if i["is_startingXI"] == True]
    return lineup


def get_squad(fixture):
    home = fixture["id_team_season_home"]
    away = fixture["id_team_season_away"]
    home_squad = [i["player_name"] for i in fixture["lineups"] if i["id_team_season"] == home and i["is_startingXI"] == True]
    away_squad = [i["player_name"] for i in fixture["lineups"] if i["id_team_season"] == away and i["is_startingXI"] == True]
    del fixture["lineups"]
    for i in range(11):
        fixture["home_player" + str(i+1)] = home_squad[i]
    for i in range(11):
        fixture["away_player" + str(i+1)] = away_squad[i]
    return fixture


def get_season(season_id):
    url = f"https://api.sportdeer.com/v1/seasons/{season_id}/fixtures?access_token={access_token}"
    content, pages = get_content_pages(url)
    fixtures = []
    for i in range(1, pages + 1):
        url = f"https://api.sportdeer.com/v1/seasons/{season_id}/fixtures?page={str(i)}&access_token={access_token}"
        fixtures += requests.get(url).json()["docs"]
    return fixtures


def get_season2(season_id):
    """
    Populated with Lineups
    """
    url = f"https://api.sportdeer.com/v1/seasons/{season_id}/fixtures?access_token={access_token}"
    content, pages = get_content_pages(url)
    fixtures = []
    for i in range(1, pages + 1):
        url = f"https://api.sportdeer.com/v1/seasons/{season_id}/fixtures?page={str(i)}&populate=lineups&access_token={access_token}"
        fixtures += [get_squad(i) for i in requests.get(url).json()["docs"]]
    return fixtures


def unnested(nested):
    new = nested["_id"]
    new["counter"] = nested["counter"]
    return new


def get_stats(fix_id, home_id, away_id):
    try:
        url = f"https://api.sportdeer.com/v1/fixtures/{fix_id}/stats?access_token={access_token}"
        data = requests.get(url).json()["docs"]
        stats = [unnested(i) for i in data]
        df = pd.DataFrame(stats)
        home = df[(df["id_team_season"] == home_id) & (df["subtype"] != "blocked_shot")].groupby("type")["counter"].sum()
        away = df[(df["id_team_season"] == away_id) & (df["subtype"] != "blocked_shot")].groupby("type")["counter"].sum()

        h_poss = home.get("ball_possession", 0)
        h_shot_on = home.get("shoton", 0)
        h_shot_off = home.get("shotoff", 0)
        h_corner = home.get("corner", 0)
        h_cross = home.get("cross", 0)
        h_offs = home.get("offside", 0)
        h_fouls = home.get("foulcommit", 0)
        h_card = home.get("card", 0)

        a_poss = away.get("ball_possession", 0)
        a_shot_on = away.get("shoton", 0)
        a_shot_off = away.get("shotoff", 0)
        a_corner = away.get("corner", 0)
        a_cross = away.get("cross", 0)
        a_offs = away.get("offside", 0)
        a_fouls = away.get("foulcommit", 0)
        a_card = away.get("card", 0)

        return fix_id, home_id, away_id, h_poss, h_shot_on, h_shot_off, h_corner, h_cross, h_offs, h_fouls, h_card, a_poss, a_shot_on, a_shot_off, a_corner, a_cross, a_offs, a_fouls, a_card
    except:
        print(f"Can't get stats for fixture {fix_id}")
        return fix_id, home_id, away_id, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None


def get_whole_season(season_id):
    df_season = pd.DataFrame(get_season2(season_id))
    print("season done")
    ids = df_season[["_id", "id_team_season_home", "id_team_season_away"]].values
    stats_dict = {}
    for i, j in enumerate(ids):
        try:
            stats_dict[i] = get_stats(*tuple(j))
            print(i)
        except:
            print(i, j)
    stats = pd.DataFrame(stats_dict).T
    stats.columns = ["_id", "home_id", "away_id", "h_poss", "h_shot_on", "h_shot_off", "h_corner", "h_cross", "h_offs", "h_fouls", "h_card", "a_poss", "a_shot_on", "a_shot_off", "a_corner", "a_cross", "a_offs", "a_fouls", "a_card"]
    df_season = df_season.merge(stats, on="_id")
    return df_season
