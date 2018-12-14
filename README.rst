====================
Football Predictions
====================

The aim of this project is to create football prediction models which can beat the bookies.


Description
===========

This project started as my final project for a data science bootcamp. The Jupyter-Notebook with the presentation (PRESENTATION.ipynb) can be found in the folder "src".

I use various machine learning and deep learning techniques in this project to create football prediction models.

Each week I will post my predictions for the Premier League below (usually updated on Tuesdays for midweek matches and Fridays for weekend matches). Starting November, statistics of my bets from the Premier League and many other leagues can be found on my `BlogaBet Account <https://dataguybets.blogabet.com/>`_.

.. table:: Predictions 14/12/18

    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |  Date  |Div|       HomeTeam        |    AwayTeam     |x_HG|x_AG|x_HC | AHC |adj_AHC|Diff |H_Odds|A_Odds|   BET    |
    +========+===+=======================+=================+====+====+=====+=====+=======+=====+======+======+==========+
    |15/12/18|E0 |Crystal Palace         |Leicester City   |1.25|1.05|-0.19|-0.25|  -0.01|-0.18|  2.23|  1.70|HOME -0.25|
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |15/12/18|E0 |Fulham                 |West Ham United  |1.35|1.36| 0.01| 0.25|   0.15|-0.14|  1.80|  2.08|          |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |15/12/18|E0 |Huddersfield Town      |Newcastle United |1.10|0.95|-0.14|-0.25|  -0.03|-0.11|  2.21|  1.71|          |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |15/12/18|E0 |Manchester City        |Everton          |2.64|0.80|-1.84|-2.00|  -1.91| 0.07|  2.04|  1.82|          |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |15/12/18|E0 |Tottenham Hotspur      |Burnley          |2.58|0.74|-1.84|-2.00|  -2.06| 0.22|  1.85|  2.00|AWAY 2.0  |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |15/12/18|E0 |Watford                |Cardiff City     |1.86|0.83|-1.03|-1.00|  -0.86|-0.17|  2.11|  1.77|HOME -1.0 |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |15/12/18|E0 |Wolverhampton Wanderers|AFC Bournemouth  |1.61|0.96|-0.65|-0.75|  -0.50|-0.15|  2.24|  1.70|HOME -0.75|
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |16/12/18|E0 |Brighton & Hove Albion |Chelsea          |0.79|1.90| 1.11| 1.00|   1.10| 0.01|  2.06|  1.81|          |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |16/12/18|E0 |Liverpool              |Manchester United|1.86|0.85|-1.02|-1.00|  -1.06| 0.04|  1.85|  2.01|          |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |16/12/18|E0 |Southampton            |Arsenal          |1.09|1.58| 0.49| 0.75|   0.58|-0.09|  1.72|  2.19|          |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
	

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
