## Mitchell Hills's 431W Project: NHL Game Database Command Line Interface Program ##

This repository contains the python script that the user will use to interact with the NHL Game Database Command Line Interface Program located in "431W Project Code.py". PostgreSQL, pgAdmin, psycopg2 was used to implement this program where the data originally came from https://www.kaggle.com/datasets/martinellis/nhl-game-data?select=team_info.csv. The original data from Kaggle was cleansed, modified, and then reduced so that the data could be imported into pgAdmin and uploaded to GitHub. You can find all the database tables, in CSV format, necessary to run the NHL Game Database Command Line Interface Program located in the "Database Tables" folder.

## NHL Game Database Command Line Interface Program Setup ##

Three separate software need to be downloaded for the correct execution on the program script:

  1. PostgreSQL - this is the relational database system that is used to store and query the necessary data for the different functionalities. The latest version can be downloaded from here -> https://www.postgresql.org/
  2. pgAdmin - this is the administration and development platform used for PostgreSQL. This software should be installed along with PostgreSQL however, if this isn't the case the latest version can be downloaded from here -> https://www.pgadmin.org/. Upon downloading pgAdmin create a local server with a username = "postgres" and a password defined by user. The user defined password will have to be updated on line 21 in "431W Project Code.py" to work correctly. Once a local server has been created import all the CSV files located in the "Database Tables" folder. When defining the attributes for each table in pgAdmin, all column names ending in "_ID" are considered primary keys for that table and every attribute should be defined as NOT NULL.
  3. Psycopg2 - this is the database adapter that the python script will use to communicate with the PostgreSQL server created in pgAdmin. The latest version can be installed by running "pip install psycopg2" in the windows command prompt.

After each of these steps has been completed the environment for the NHL Game Database Command Line Interface Program is finished and can now be executed properly.
