
def marktwerte(df, werte):
    werte = werte.set_index("Team").unstack().reset_index()
    werte.columns = ["season", "team", "value"]
    werte.season = werte.season.apply(int)
    werte["value"] = werte.groupby("season")["value"].transform(lambda x: (x - x.mean()) / x.std())
    df = df.merge(werte, how="left", left_on=["season", "HomeTeam"], right_on=["season", "team"])
    df = df.merge(werte, how="left", left_on=["season", "AwayTeam"], right_on=["season", "team"])
    new_names = {"value_x": "H_value", "value_y": "A_value"}
    df.rename(new_names, axis="columns", inplace=True)
    del df["team_x"]
    del df["team_y"]
    return df
