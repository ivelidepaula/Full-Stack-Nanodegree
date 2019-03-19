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

# Connect to postgreSQL database.
def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")

# Return query results
def get_query_results(query):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
return results

#Display results for the first two questions
def print_query_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print (
            "\t", index+1, "--", results[0],
            "\t - ", str(results[1]), "views")

#Display results for the last question
def print_error_results(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print ("\t", results[0], "--", str(results[1]) + "% errors")

#Store and print the final results
if __name__ == '__main__':
    popular_articles_results = get_query_results(queryOne), questionOne
    popular_authors_results = get_query_results(queryTwo), questionTwo
    load_error_days = get_query_results(queryThree), questionThree
    print_query_results(popular_articles_results)
    print_query_results(popular_authors_results)
    print_error_results(load_error_days)
