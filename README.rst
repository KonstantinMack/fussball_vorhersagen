====================
Football Predictions
====================

The aim of this project is to create football prediction models which can beat the bookies.


Description
===========

This project started as my final project for a data science bootcamp. The Jupyter-Notebook with the presentation (PRESENTATION.ipynb) can be found in the folder "src".

I use various machine learning and deep learning techniques in this project to create football prediction models.

Each week I will post my predictions for the Premier League below (usually updated on Tuesdays for midweek matches and Fridays for weekend matches). Starting November, statistics of my bets from the Premier League and many other leagues can be found on my `BlogaBet Account <https://dataguybets.blogabet.com/>`_.

.. table:: Predictions 26/12/18

    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |   Date   |Div|       HomeTeam       |       AwayTeam        |x_HG|x_AG|x_HC | AHC |adj_AHC|Diff |H_Odds|A_Odds|   BET    |
    +==========+===+======================+=======================+====+====+=====+=====+=======+=====+======+======+==========+
    |26/12/2018|E0 |Brighton & Hove Albion|Arsenal                |0.93|1.70| 0.78| 1.00|   0.80|-0.02|  1.68|  2.26|          |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |26/12/2018|E0 |Burnley               |Everton                |0.94|1.56| 0.62| 0.75|   0.58| 0.04|  1.72|  2.20|          |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |26/12/2018|E0 |Crystal Palace        |Cardiff City           |1.80|0.74|-1.05|-1.00|  -0.84|-0.21|  2.13|  1.76|HOME -1.0 |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |26/12/2018|E0 |Fulham                |Wolverhampton Wanderers|1.18|1.30| 0.12| 0.25|   0.19|-0.07|  1.85|  2.03|          |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |26/12/2018|E0 |Leicester City        |Manchester City        |0.86|1.97| 1.11| 1.50|   1.45|-0.34|  1.87|  2.00|HOME 1.5  |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |26/12/2018|E0 |Liverpool             |Newcastle United       |2.51|0.64|-1.87|-2.00|  -2.13| 0.26|  1.77|  2.11|AWAY 2.0  |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |26/12/2018|E0 |Manchester United     |Huddersfield Town      |2.33|0.80|-1.52|-1.50|  -1.68| 0.16|  1.70|  2.21|AWAY 1.5  |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |26/12/2018|E0 |Tottenham Hotspur     |AFC Bournemouth        |2.10|0.85|-1.25|-1.50|  -1.48| 0.23|  1.96|  1.91|AWAY 1.5  |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |26/12/2018|E0 |Watford               |Chelsea                |0.97|1.64| 0.68| 1.00|   0.78|-0.10|  1.66|  2.28|          |
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |27/12/2018|E0 |Southampton           |West Ham United        |1.50|1.02|-0.48|-0.25|  -0.24|-0.24|  1.94|  1.94|HOME -0.25|
    +----------+---+----------------------+-----------------------+----+----+-----+-----+-------+-----+------+------+----------+



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
