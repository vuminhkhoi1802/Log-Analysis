
# Queries for the database
# 1. What are the most popular three articles of all time?
popular_three_articles = """select articles.title, count(*) as num 
			from log, articles
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by num desc
            limit 3;"""

# 2. Who are the most popular article authors of all time?
popular_authors = """select authors.name, count(*) as num 
			from articles, authors, log
			where log.status = '200 OK'
			and authors.id = articles.author
			and articles.slug = substr(log.path, 10)
			group by authors.name 
			order by num desc; """

# 3. On which days did more than 1% of requests lead to errors?
error_days = """select time, failure_percentage 
			from percentage_total
			where failure_percentage > 1;"""