# Logs Analysis

### 1) What are the most popular three articles of all time?
>**Query:** `SELECT title, views
  FROM articles
  INNER JOIN
      (SELECT path, count(path) AS views
                     FROM log
                     GROUP BY log.path) AS log
  ON log.path = '/article/' || articles.slug
  ORDER BY views desc limit 3;`

>**Returns:**
The 3 Most Popular Stories Are:
Candidate is jerk, alleges rival -- 338647 views
Bears love berries, alleges bear -- 253801 views
Bad things gone, say good people -- 170098 views

### 2) Who are the most popular article authors of all time?
>**Query:** `SELECT date, percent_errors
  FROM (SELECT errors.day AS date, (cast(errors.total_errors AS float)
          / cast(views.total_views AS float) * 100) AS percent_errors
          FROM errors
          JOIN views
          ON errors.day = views.day) AS most_errors
  GROUP BY most_errors.date, most_errors.percent_errors
  HAVING SUM(percent_errors) >= 1.0
  ORDER BY percent_errors desc;`

>**Returns:**
> The Most Popular Authors Are:
Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views

### 3) On which days did more than 1% of requests lead to errors?
>**Query:** `SELECT titlename.name, count(path) AS views
  FROM log,
      (SELECT name, slug
                     FROM authors
                     JOIN articles
                     ON authors.id = articles.author) AS titlename
  WHERE log.path = '/article/' ||titlename.slug
  GROUP BY titlename.name
  ORDER BY views desc;`

>**Created view _errors_:** `create view errors as select date(time) as day, count(*) as total_errors from log where status != '200 OK' group by day order by total_errors;`

>**Created view _views_:** `create view views as select date(time) as day, count(*) as total_views from log group by day order by total_views;`

>**Returns:**
> The Day with the Most Errors Was:
July 17, 2016 -- 2.26% errors
