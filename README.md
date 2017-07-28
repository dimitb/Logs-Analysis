# Logs Analysis

### Introduction
>The Logs Analysis project is the third project in the Udacity Full-Stack Nanodegree program that displays a simple text output of three different questions regarding a pre-established database for a news site. The database queries are written in psql (PostgreSQL) and answer the following:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

### Getting Started
>The Logs Analysis project was written using Python and PSQL with a Vagrant configured VirtualBox vm. The following versions were used:
- Python 3 - 3.6.1 [Download](https://www.python.org/downloads/)
- psql (PostgreSQL) - 9.5.7 [Download](https://www.postgresql.org/download/)
- pyscopg2 - 2.7.1 [Download](http://initd.org/psycopg/download/)
- Vagrant - 1.9.7 [Download](https://www.vagrantup.com/downloads.html)
- VirtualBox - 5.1.26 [Download](https://www.virtualbox.org/wiki/Downloads)

>To ensure compatibility and the queries run as intended, please make sure you have the versions listed above, or better, installed.

### Installation/Creating the Database
>To create and connect to the news database to run the quries, download the _newsdata.zip_ file. The zip file contains a _vagrantfile_, which will create the news database and _newsdat.sql_, which contains the database schema and data.
>
>Once downloaded, change to the **vagrant** directory from your terminal and start the virtual machine by running the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it.

>Once `vagrant up` is finished running, you'll be returned to your shell prompt. From here, run `vagrant ssh` to log into the Linux VM install. After logging into your vm, run the command `psql -d news -f newsdata.sql` to load the database's data. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

>The project also uses two psql custom created views in the third query (_On which days did more than 1% of requests lead to errors?_).

>To create the views, connect to the _news_ database and copy/paste and run the following statements in the terminal:
- `create view errors as select date(time) as day, count(*) as total_errors from log where status != '200 OK' group by day order by total_errors;`
- `create view views as select date(time) as day, count(*) as total_views from log group by day order by total_views;`

>After creating the views in the _news_ database, download the _logs-analysis.py_ file from the _Logs Analysis_ repository and run the file with the command `python3 logs_analysis.py` in the terminal. Running the file will start the psql queries and produce a series of simple text lists displaying the answers to the three queries (NOTE: all three queries are run from the same python file).

### Miscellany
>A copy of the queries and their output (_logs-analysis-answers.md_) can be found in the repository as well, stating the correct answers to each question.

>Make sure to place the _logs-analysis.py_ file in the same directory as your Vagrant folder/file and your database file.
