#! /usr/bin/env python3
import psycopg2

# 1. What are the most popular three articles of all time?

questionOne='What are the most popular three articles of all time?'
queryOne="""
    select 
        articles.title, 
        count(*) as views
    from 
        articles 
        inner join log on log.path like concat('%', articles.slug, '%')
    where 
        log.status like '%200%' 
    group by 
        articles.title, 
        log.path 
    order by 
        views desc 
    limit 
        3"""


# 2. Who are the most popular article authors of all time?
questionTwo='Who are the most popular article authors of all time?'
queryTwo="""
    select 
        authors.name,
        sum(article_view.views) as views 
    from
        article_view,
        authors 
    where 
        authors.id = article_view.author
    group by 
        authors.name 
    order by 
        views des"""

# 3. On which days did more than 1% of requests lead to errors?
questionThree='On which days did more than 1% of requests lead to errors?'
queryThree="""
    select 
        * 
    from 
        error_log 
    where 
        Percent_Error > 1"""