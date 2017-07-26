# Logs Analysis

### 1) What are the most popular three articles of all time?
>**Query:** `select articles.title, count(log.path) as views from articles, log
  where log.path like '%'||articles.slug group by articles.title
  order by views desc limit 3;`

>**Returns:**
The 3 Most Popular Stories Are:
Candidate is jerk, alleges rival -- 338647 views
Bears love berries, alleges bear -- 253801 views
Bad things gone, say good people -- 170098 views

### 2) Who are the most popular article authors of all time?
>**Query:** `select titlename.name, count(log.path) as views from log,
  (select name, slug from authors join articles on
  authors.id = articles.author) as titlename
  where log.path like '%'||titlename.slug group by titlename.name
  order by views desc;`

>**Returns:**
> The Most Popular Authors Are:
Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views

### 3) On which days did more than 1% of requests lead to errors?
>**Query:** `select errors.day, cast(errors.total_errors as float) /
  cast(views.total_views as float) * 100 as percent_errors from errors
  join views on errors.day = views.day
  order by percent_errors desc limit 1;`

>**Created view _errors_:** `create view errors as select date(time) as day, count(*) as total_errors from log where status != '200 OK' group by day order by total_errors;`

>**Created view _views_:** `create view views as select date(time) as day, count(*) as total_views from log group by day order by total_views;`

>**Returns:**
> The Day with the Most Errors Was:
July 17, 2016 -- 2.26% errors
