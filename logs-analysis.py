#!/usr/bin/env python3
import psycopg2


top_stories = (    # psql query to return the top stories
    """
    SELECT title, views
    FROM articles
    INNER JOIN
        (SELECT path, count(path) AS views
                       FROM log
                       GROUP BY log.path) AS log
    ON log.path = '/article/' || articles.slug
    ORDER BY views desc limit 3;
    """
)


def get_top_stories():
    """Return results for get_top_stories query."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(top_stories)
    story_rows = c.fetchall()
    print("The 3 Most Popular Stories Are:")
    for title, views in story_rows:
        print("\"{}\" -- {} views".format(title, views))
    db.close


top_authors = (    # psql query to return the top authors
    """
    SELECT titlename.name, count(path) AS views
    FROM log,
        (SELECT name, slug
                       FROM authors
                       JOIN articles
                       ON authors.id = articles.author) AS titlename
    WHERE log.path = '/article/' ||titlename.slug
    GROUP BY titlename.name
    ORDER BY views desc;;
    """
)


def get_top_authors():
    """Return results from get_top_authors query."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(top_authors)
    author_rows = c.fetchall()
    print("The Most Popular Authors Are:")
    for name, views in author_rows:
        print("\"{}\" -- {} views".format(name, views))
    db.close()


most_errors = (    # psql query to return the days with most errors
    """
    SELECT date, percent_errors
    FROM (SELECT errors.day AS date, (cast(errors.total_errors AS float)
            / cast(views.total_views AS float) * 100) AS percent_errors
            FROM errors
            JOIN views
            ON errors.day = views.day) AS most_errors
    GROUP BY most_errors.date, most_errors.percent_errors
    HAVING SUM(percent_errors) >= 1.0
    ORDER BY percent_errors desc;
    """
)


def get_days_errors_over_1_percent():
    """Return the results for the get_days_errors_over_1_percent query."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(most_errors)
    errors_rows = c.fetchall()
    print("The Day with the Most Errors Was:")
    for row in errors_rows:
        print('{0:%B %d, %Y} -- {1:.2f}% errors'.format(row[0], row[1]))
    db.close()


if __name__ == '__main__':  # Ensures each function runs only when called upon
    get_top_stories()
    print("")
    get_top_authors()
    print("")
    get_days_errors_over_1_percent()
    print("")
