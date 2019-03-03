====================
Football Predictions
====================

The aim of this project is to create football prediction models which can beat the bookies.


Description
===========

This project started as my final project for a data science bootcamp. The Jupyter-Notebook with the presentation (PRESENTATION.ipynb) can be found in the folder "src".

I use various machine learning and deep learning techniques in this project to create football prediction models.

Each week I will post my predictions for the Premier League below (usually updated on Tuesdays for midweek matches and Fridays for weekend matches). Starting November, statistics of my bets from the Premier League and many other leagues can be found on my `BlogaBet Account <https://dataguybets.blogabet.com/>`_.

.. table:: Predictions 02/03/19

    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |   Date   |Div|       HomeTeam        |    AwayTeam     |x_HG|x_AG|x_HC | AHC |adj_AHC|Diff |H_Odds|A_Odds|   BET    |
    +==========+===+=======================+=================+====+====+=====+=====+=======+=====+======+======+==========+
    |02/03/2019|E0 |AFC Bournemouth        |Manchester City  |0.87|2.32| 1.45| 2.00|   1.95|-0.50|  1.87|  1.99|HOME 2.0  |
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |02/03/2019|E0 |Brighton & Hove Albion |Huddersfield Town|1.49|0.79|-0.70|-0.75|  -0.63|-0.07|  2.08|  1.80|          |
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |02/03/2019|E0 |Burnley                |Crystal Palace   |1.16|1.19| 0.03| 0.25|   0.05|-0.02|  1.68|  2.26|          |
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |02/03/2019|E0 |Manchester United      |Southampton      |2.10|0.82|-1.28|-1.00|  -1.17|-0.11|  1.72|  2.19|          |
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |02/03/2019|E0 |Tottenham Hotspur      |Arsenal          |1.62|1.09|-0.53|-0.25|  -0.39|-0.14|  1.76|  2.13|          |
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |02/03/2019|E0 |West Ham United        |Newcastle United |1.43|0.93|-0.51|-0.25|  -0.35|-0.16|  1.80|  2.08|HOME -0.25|
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |02/03/2019|E0 |Wolverhampton Wanderers|Cardiff City     |2.00|0.76|-1.24|-1.00|  -1.06|-0.18|  1.86|  2.00|HOME -1.0 |
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |03/03/2019|E0 |Everton                |Liverpool        |0.90|1.69| 0.79| 1.00|   0.88|-0.09|  1.78|  2.10|          |
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |03/03/2019|E0 |Fulham                 |Chelsea          |0.86|1.89| 1.03| 1.00|   1.07|-0.04|  2.02|  1.84|          |
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+
    |03/03/2019|E0 |Watford                |Leicester City   |1.27|1.17|-0.10|-0.25|  -0.11| 0.01|  2.11|  1.78|          |
    +----------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+----------+


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
