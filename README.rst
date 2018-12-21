====================
Football Predictions
====================

The aim of this project is to create football prediction models which can beat the bookies.


Description
===========

This project started as my final project for a data science bootcamp. The Jupyter-Notebook with the presentation (PRESENTATION.ipynb) can be found in the folder "src".

I use various machine learning and deep learning techniques in this project to create football prediction models.

Each week I will post my predictions for the Premier League below (usually updated on Tuesdays for midweek matches and Fridays for weekend matches). Starting November, statistics of my bets from the Premier League and many other leagues can be found on my `BlogaBet Account <https://dataguybets.blogabet.com/>`_.

.. table:: Predictions 21/12/18

    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |   Date   |Div|       HomeTeam        |       AwayTeam       |x_HG|x_AG|x_HC | AHC |adj_AHC|Diff |H_Odds|A_Odds|   BET    |
    +==========+===+=======================+======================+====+====+=====+=====+=======+=====+======+======+==========+
    |21/12/2018|E0 |Wolverhampton Wanderers|Liverpool             |0.81|1.69| 0.88| 1.00|   0.95|-0.07|  1.87|  2.01|          |
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |22/12/2018|E0 |Arsenal                |Burnley               |2.48|0.76|-1.72|-1.50|  -1.70|-0.02|  1.68|  2.24|          |
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |22/12/2018|E0 |AFC Bournemouth        |Brighton & Hove Albion|1.65|0.91|-0.74|-0.75|  -0.53|-0.21|  2.21|  1.71|HOME -0.75|
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |22/12/2018|E0 |Cardiff City           |Manchester United     |0.91|1.84| 0.93| 1.00|   0.94|-0.01|  1.86|  2.01|          |
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |22/12/2018|E0 |Chelsea                |Leicester City        |2.13|0.79|-1.34|-1.50|  -1.47| 0.13|  1.97|  1.89|          |
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |22/12/2018|E0 |Huddersfield Town      |Southampton           |1.04|1.16| 0.12| 0.25|   0.09| 0.03|  1.73|  2.18|          |
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |22/12/2018|E0 |Manchester City        |Crystal Palace        |2.73|0.69|-2.03|-2.50|  -2.36| 0.33|  2.11|  1.77|AWAY 2.5  |
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |22/12/2018|E0 |Newcastle United       |Fulham                |1.57|0.93|-0.64|-0.25|  -0.43|-0.21|  1.71|  2.21|HOME -0.25|
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |22/12/2018|E0 |West Ham United        |Watford               |1.42|1.14|-0.27|-0.25|  -0.19|-0.08|  2.01|  1.87|          |
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
    |23/12/2018|E0 |Everton                |Tottenham Hotspur     |1.21|1.31| 0.10| 0.25|   0.23|-0.13|  1.90|  1.97|          |
    +----------+---+-----------------------+----------------------+----+----+-----+-----+-------+-----+------+------+----------+
	

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
