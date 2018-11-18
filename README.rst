====================
Football Predictions
====================

The aim of this project is to create football prediction models which can beat the bookies.


Description
===========

This project started as my final project for a data science bootcamp. The Jupyter-Notebook with the presentation (presentation.ipynb) can be found in the folder "src".

I use various machine learning and deep learning techniques in this project to create football prediction models.

Each week I will post my predictions for the Premier League below (usually updated on Tuesdays for midweek matches and Fridays for weekend matches). Starting November, statistics of my bets from the Premier League and many other leagues can be found on my `BlogaBet Account <https://dataguybets.blogabet.com/>`_.

+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|  Date  |Div|    HomeTeam     |       AwayTeam        |x_HG|x_AG|x_HC | AHC  |adj_AHC|Diff |H_Odds|A_Odds|    BET    |
+========+===+=================+=======================+====+====+=====+======+=======+=====+======+======+===========+
|10/11/18|E0 |Cardiff City     |Brighton & Hove Albion |1.27|1.02|-0.25|-0.25 |  -0.10|-0.15|  2.15|  1.75|HOME -0.25 |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|10/11/18|E0 |Crystal Palace   |Tottenham Hotspur      |1.00|1.50| 0.50| 0.75 |   0.65|-0.15|  1.78|  2.10|HOME 0.75  |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|10/11/18|E0 |Huddersfield Town|West Ham United        |0.88|1.17| 0.29| 0.25 |   0.24| 0.05|  1.91|  1.96|           |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|10/11/18|E0 |Leicester City   |Burnley                |2.01|0.84|-1.17|-1.00 |  -1.07|-0.10|  1.82|  2.06|           |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|10/11/18|E0 |Newcastle United |AFC Bournemouth        |1.22|1.17|-0.04| 0.25 |   0.11|-0.15|  1.72|  2.20|HOME 0.25  |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|10/11/18|E0 |Southampton      |Watford                |1.29|1.13|-0.15|-0.25 |  -0.12|-0.03|  2.12|  1.78|           |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|11/11/18|E0 |Arsenal          |Wolverhampton Wanderers|1.74|1.02|-0.72|-1.00 |  -0.87| 0.15|  2.12|  1.76|AWAY 1.0   |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|11/11/18|E0 |Chelsea          |Everton                |2.19|0.89|-1.30|-1.00 |  -1.19|-0.11|  1.65|  2.29|           |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|11/11/18|E0 |Liverpool        |Fulham                 |2.68|0.73|-1.95|-2.75 |  -2.68| 0.73|  2.00|  1.87|AWAY 2.75  |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+
|11/11/18|E0 |Manchester City  |Manchester United      |2.43|0.90|-1.53|-1.25 |  -1.34|-0.19|  1.80|  2.08|HOME -1.25 |
+--------+---+-----------------+-----------------------+----+----+-----+------+-------+-----+------+------+-----------+


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
