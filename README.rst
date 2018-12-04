====================
Football Predictions
====================

The aim of this project is to create football prediction models which can beat the bookies.


Description
===========

This project started as my final project for a data science bootcamp. The Jupyter-Notebook with the presentation (PRESENTATION.ipynb) can be found in the folder "src".

I use various machine learning and deep learning techniques in this project to create football prediction models.

Each week I will post my predictions for the Premier League below (usually updated on Tuesdays for midweek matches and Fridays for weekend matches). Starting November, statistics of my bets from the Premier League and many other leagues can be found on my `BlogaBet Account <https://dataguybets.blogabet.com/>`_.

.. table:: Predictions 04/12/18

    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |  Date  |Div|       HomeTeam        |    AwayTeam     |x_HG|x_AG|x_HC | AHC |adj_AHC|Diff |H_Odds|A_Odds|   BET   |
    +========+===+=======================+=================+====+====+=====+=====+=======+=====+======+======+=========+
    |04/12/18|E0 |AFC Bournemouth        |Huddersfield Town|1.82|0.87|-0.95|-1.00|  -0.76|-0.19|  2.23|  1.69|HOME -1.0|
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |04/12/18|E0 |Brighton & Hove Albion |Crystal Palace   |1.04|1.09| 0.05| 0.25|   0.05| 0.00|  1.68|  2.26|------   |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |04/12/18|E0 |Watford                |Manchester City  |0.90|2.07| 1.17| 1.50|   1.57|-0.40|  2.02|  1.84|HOME 1.5 |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |04/12/18|E0 |West Ham United        |Cardiff City     |1.80|0.81|-0.99|-1.00|  -0.86|-0.13|  2.11|  1.77|------   |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |05/12/18|E0 |Burnley                |Liverpool        |0.74|2.07| 1.33| 1.50|   1.61|-0.28|  2.07|  1.79|HOME 1.5 |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |05/12/18|E0 |Everton                |Newcastle United |1.88|0.71|-1.17|-1.00|  -0.94|-0.23|  2.01|  1.85|HOME -1.0|
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |05/12/18|E0 |Fulham                 |Leicester City   |1.19|1.42| 0.23| 0.25|   0.15| 0.08|  1.81|  2.08|------   |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |05/12/18|E0 |Manchester United      |Arsenal          |1.45|1.34|-0.11|-0.25|  -0.13| 0.02|  2.08|  1.80|------   |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |05/12/18|E0 |Tottenham Hotspur      |Southampton      |2.06|0.85|-1.21|-1.00|  -1.28| 0.07|  1.58|  2.44|------   |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+
    |05/12/18|E0 |Wolverhampton Wanderers|Chelsea          |0.97|1.63| 0.66| 1.00|   0.74|-0.08|  1.60|  2.41|------   |
    +--------+---+-----------------------+-----------------+----+----+-----+-----+-------+-----+------+------+---------+

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
