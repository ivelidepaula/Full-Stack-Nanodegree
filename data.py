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
        count(*) as views 
    from 
    articles 
    inner join authors on articles.author = authors.id 
    inner join log on concat('/article/', articles.slug) = log.path 
    where 
        log.status like '%200%' 
    group by 
        authors.name 
    order by 
        views desc"""

# 3. On which days did more than 1% of requests lead to errors?