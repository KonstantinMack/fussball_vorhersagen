====================
Football Predictions
====================

The aim of this project is to create football prediction models which can beat the bookies.


Description
===========

This project started as my final project for a data science bootcamp. The Jupyter-Notebook with the presentation (PRESENTATION.ipynb) can be found in the folder "src".

I use various machine learning and deep learning techniques in this project to create football prediction models.

Each week I will post my predictions for the Premier League below (usually updated on Tuesdays for midweek matches and Fridays for weekend matches). Starting November, statistics of my bets from the Premier League and many other leagues can be found on my `BlogaBet Account <https://dataguybets.blogabet.com/>`_.

.. table:: Predictions 07/12/18

    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |  Date  |Div|    HomeTeam     |       AwayTeam        |x_HG|x_AG|x_HC | AHC |adj_AHC|Diff |H_Odds|A_Odds|   BET    |
    +========+===+=================+=======================+====+====+=====+=====+=======+=====+======+======+==========+
    |08/12/18|E0 |Arsenal          |Huddersfield Town      |2.27|0.86|-1.41|-1.50|  -1.60| 0.19|  1.80|  2.06|AWAY 1.5  |
    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |08/12/18|E0 |AFC Bournemouth  |Liverpool              |0.93|1.77| 0.85| 1.00|   0.98|-0.13|  1.90|  1.96|          |
    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |08/12/18|E0 |Burnley          |Brighton & Hove Albion |1.14|1.17| 0.03| 0.25|   0.03| 0.00|  1.65|  2.31|          |
    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |08/12/18|E0 |Cardiff City     |Southampton            |1.16|1.26| 0.10| 0.25|   0.07| 0.03|  1.70|  2.22|          |
    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |08/12/18|E0 |Chelsea          |Manchester City        |1.11|1.59| 0.48| 0.75|   0.57|-0.09|  1.70|  2.24|          |
    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |08/12/18|E0 |Leicester City   |Tottenham Hotspur      |1.02|1.45| 0.42| 0.25|   0.44|-0.02|  2.17|  1.73|          |
    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |08/12/18|E0 |Manchester United|Fulham                 |2.35|0.83|-1.52|-1.50|  -1.43|-0.09|  2.02|  1.83|          |
    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |08/12/18|E0 |West Ham United  |Crystal Palace         |1.37|0.96|-0.41|-0.25|  -0.25|-0.16|  1.93|  1.94|HOME -0.25|
    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |09/12/18|E0 |Newcastle United |Wolverhampton Wanderers|1.07|1.14| 0.07| 0.25|   0.05| 0.02|  1.68|  2.25|          |
    +--------+---+-----------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |10/12/18|E0 |Everton          |Watford                |1.68|0.87|-0.81|-1.00|  -0.63|-0.18|  2.39|  1.61|HOME -1.0 |
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
