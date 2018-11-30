====================
Football Predictions
====================

The aim of this project is to create football prediction models which can beat the bookies.


Description
===========

This project started as my final project for a data science bootcamp. The Jupyter-Notebook with the presentation (PRESENTATION.ipynb) can be found in the folder "src".

I use various machine learning and deep learning techniques in this project to create football prediction models.

Each week I will post my predictions for the Premier League below (usually updated on Tuesdays for midweek matches and Fridays for weekend matches). Starting November, statistics of my bets from the Premier League and many other leagues can be found on my `BlogaBet Account <https://dataguybets.blogabet.com/>`_.

+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|  Date  |Div|    HomeTeam     |       AwayTeam        |x_HG|x_AG|x_HC | AHC |adj_AHC|Diff |H_Odds|A_Odds|   BET    |
+========+===+=================+=======================+====+====+=====+=====+=======+=====+======+======+==========+
|30/11/18|E0 |Cardiff City     |Wolverhampton Wanderers|0.97|1.40| 0.43| 0.25|   0.31| 0.12|  2.00|  1.87|          |
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|01/12/18|E0 |Crystal Palace   |Burnley                |1.80|0.74|-1.06|-1.00|  -0.87|-0.19|  2.09|  1.79|HOME -1.0 |
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|01/12/18|E0 |Huddersfield Town|Brighton & Hove Albion |1.11|0.88|-0.23|-0.25|  -0.13|-0.10|  2.08|  1.81|          |
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|01/12/18|E0 |Leicester City   |Watford                |1.38|1.00|-0.38|-0.25|  -0.25|-0.13|  1.93|  1.94|          |
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|01/12/18|E0 |Manchester City  |AFC Bournemouth        |2.88|0.79|-2.09|-2.50|  -2.58| 0.49|  1.83|  2.03|AWAY 2.5  |
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|01/12/18|E0 |Newcastle United |West Ham United        |1.29|0.99|-0.30|-0.25|  -0.11|-0.19|  2.10|  1.79|HOME -0.25|
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|01/12/18|E0 |Southampton      |Manchester United      |1.01|1.57| 0.56| 0.75|   0.57|-0.01|  1.71|  2.21|          |
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|02/12/18|E0 |Arsenal          |Tottenham Hotspur      |1.40|1.30|-0.10|-0.25|  -0.03|-0.07|  2.21|  1.71|          |
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|02/12/18|E0 |Chelsea          |Fulham                 |2.59|0.78|-1.81|-2.00|  -2.10| 0.29|  1.81|  2.06|AWAY 2.0  |
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
|02/12/18|E0 |Liverpool        |Everton                |2.05|0.75|-1.30|-1.00|  -1.27|-0.03|  1.59|  2.41|          |
+--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+


Abbreviations:

- x_HG -> expected goals by the home team
- x_AG -> expected goals by the away team
- x_HC -> expected goal difference
- AHC -> bookie's asian handicap line
- adj_AHC -> bookie's ahc line adjusted for the odds (basically representing the bookie's expected goal difference)
- Diff -> difference between x_HC and adj_AHC
- H_Odds -> bookie's ahc odds for the home team
- A_Odds -> bookie's ahc odds for the away team
- BET -> suggested bet (if Diff is >=0.15 or <=-0.15 respectively)
