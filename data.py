import psycopg2

# 1. What are the most popular three articles of all time?

questionOne='What are the most popular three articles of all time?'
queryOne=(
    select articles.title, count(*) as views
    from articles inner join log on log.path
    like concat('%', articles.slug, '%')
    where log.status like '%200%' 
    group by "articles.title, log.path 
    order by views desc limit 3
)

# 2. Who are the most popular article authors of all time?

# 3. On which days did more than 1% of requests lead to errors?

