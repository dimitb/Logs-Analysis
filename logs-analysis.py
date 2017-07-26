#!/usr/bin/env python3
import psycopg2
import datetime


top_3_stories = (
    """
    select articles.title, count(log.path) as views from articles, log
    where log.path like '%'||articles.slug group by articles.title
    order by views desc limit 3;
    """
)


def get_top_stories():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query_1 = top_3_stories
    c.execute(query_1)
    story_rows = c.fetchall()
    print("The 3 Most Popular Stories Are:")
    for row in story_rows:
        print(row[0], "--", row[1], "views")
    db.close


top_authors = (
    """
    select titlename.name, count(log.path) as views from log,
    (select name, slug from authors join articles on
    authors.id = articles.author) as titlename
    where log.path like '%'||titlename.slug group by titlename.name
    order by views desc;
    """
)


def get_top_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query_2 = top_authors
    c.execute(query_2)
    author_rows = c.fetchall()
    print("The Most Popular Authors Are:")
    for row in author_rows:
        print(row[0], "--", row[1], "views")
    db.close()


most_errors_day = (
    """
    select errors.day, cast(errors.total_errors as float) /
    cast(views.total_views as float) * 100 as percent_errors from errors
    join views on errors.day = views.day
    order by percent_errors desc limit 1;
    """
)


def get_most_errors_day():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query_3 = most_errors_day
    c.execute(query_3)
    errors_rows = c.fetchall()
    print("The Day with the Most Errors Was:")
    for row in errors_rows:
        print(('{:%B %d, %Y}'.format(row[0])), "--",
              ('{:02.2f}'.format(row[1])) + "%", 'errors')
    db.close()


get_top_stories()
print("")
get_top_authors()
print("")
get_most_errors_day()
print("")
