====================
Football Predictions
====================

The aim of this project is to create football prediction models which can beat the bookies.


Description
===========

This project started as my final project for a data science bootcamp. The Jupyter-Notebook with the presentation (PRESENTATION.ipynb) can be found in the folder "src".

I use various machine learning and deep learning techniques in this project to create football prediction models.

Each week I will post my predictions for the Premier League below (usually updated on Tuesdays for midweek matches and Fridays for weekend matches). Starting November, statistics of my bets from the Premier League and many other leagues can be found on my `BlogaBet Account <https://dataguybets.blogabet.com/>`_.

.. table:: Predictions 29/12/18

    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |   Date   |Div|       HomeTeam       |       AwayTeam        |x_HG|x_AG|x_HC | AHC |adj_AHC|Diff |H_Odds|A_Odds|   BET   |
    +==========+===+======================+=======================+====+====+=====+=====+=======+=====+======+======+=========+
    |29/12/2018|E0 |Brighton & Hove Albion|Everton                |1.01|1.42| 0.41| 0.25|   0.29| 0.12|  1.98|  1.89|         |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |29/12/2018|E0 |Fulham                |Huddersfield Town      |1.45|0.99|-0.46|-0.25|  -0.39|-0.07|  1.75|  2.15|         |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |29/12/2018|E0 |Leicester City        |Cardiff City           |1.85|0.75|-1.10|-1.00|  -0.94|-0.16|  2.00|  1.88|HOME -1.0|
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |29/12/2018|E0 |Liverpool             |Arsenal                |2.05|0.84|-1.21|-1.00|  -1.13|-0.08|  1.77|  2.13|         |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |29/12/2018|E0 |Tottenham Hotspur     |Wolverhampton Wanderers|2.09|0.78|-1.31|-1.50|  -1.36| 0.05|  2.10|  1.78|         |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |29/12/2018|E0 |Watford               |Newcastle United       |1.63|0.85|-0.77|-1.00|  -0.51|-0.26|  2.54|  1.55|HOME -1.0|
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |30/12/2018|E0 |Burnley               |West Ham United        |1.16|1.38| 0.23| 0.25|   0.24|-0.01|  1.92|  1.95|         |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |30/12/2018|E0 |Crystal Palace        |Chelsea                |0.91|1.55| 0.64| 1.00|   0.78|-0.14|  1.66|  2.30|         |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |30/12/2018|E0 |Manchester United     |AFC Bournemouth        |2.33|0.88|-1.46|-1.50|  -1.44|-0.02|  2.01|  1.86|         |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+
    |30/12/2018|E0 |Southampton           |Manchester City        |0.83|2.15| 1.32| 1.50|   1.52|-0.20|  1.96|  1.91|HOME 1.5 |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+---------+


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
