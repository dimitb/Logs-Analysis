# Logs Analysis

### Introduction
>The Logs Analysis project is the third project in the Udacity Full-Stack Nanodegree program that displays a simple text output of three different questions regarding a pre-established database for a news site. The database queries are written in psql (PostgreSQL) and answer the following:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

### Getting Started
>The Logs Analysis project runs using the Python module _DB-API_ and was written using Python 3. To ensure compatibility, make sure you have the latest update of Python 3 installed on your system (Download Python [here](https://www.python.org/downloads/)).

>The project also uses two psql custom created views in the third query (_On which days did more than 1% of requests lead to errors?_).

>To create the views, connect to the _news_ database and copy/paste and run the following statements in the terminal:
- `create view errors as select date(time) as day, count(*) as total_errors from log where status != '200 OK' group by day order by total_errors;`
- `create view views as select date(time) as day, count(*) as total_views from log group by day order by total_views;`

>After creating the views in the _news_ database, download the _logs-analysis.py_ file from the _Logs Analysis_ repository and run the file with the command `python3 logs_analysis.py` in the terminal. Running the file will start the psql queries and produce a series of simple text lists displaying the answers to the three queries (NOTE: all three queries are run from the same python file).

### Miscellany
>A copy of the queries and their output (_logs-analysis-answers.md_) can be found in the repository as well, stating the correct answers to each question.

>Make sure to place the _logs-analysis.py_ file in the same directory as your vagrant folder/file and your database file.
