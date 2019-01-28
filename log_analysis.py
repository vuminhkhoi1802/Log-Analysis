#!/usr/bin/env python3

import os

import psycopg2

# Import SQL queries from a separate queries file
from queries import *

db_name = "news"
text_file = "log_analysis.txt"


# Query the database, open & close the Connection to the database


def db_query(sql_request):
	try:
		db = psycopg2.connect(database=db_name)
		c = db.cursor()
		c.execute(sql_request)
		results = c.fetchall()
		db.close()
		return results
	except OSError:
		print("\n Cannot connect to the database \n")
		pass


# Writing the report
# Print the title of the report


def print_title(title):
	print('\n\t' + title + '\n')


# Remove the current text file before appending new data


def remove_text_file(file):
	try:
		os.remove(file)
		print("\n The existing result file log_analysis.txt is removed \n")
	except OSError:
		print("\n The log_analysis.txt does not exist! \n")
		pass


# Write all the output of queries to a text file


def output_to_file(output):
	f = open('log_analysis.txt', 'a')
	f.write(output + '\n')
	f.close()


# Print and write to file the top three articles
def top_3_articles():
	top_three_articles = db_query(popular_three_articles)
	title = "Top 3 articles"
	print_title(title)
	output_to_file('\n' + title + '\n')
	for title, num in top_three_articles:
		out_top_3 = "{0} -- {1} views".format(title, num)
		print(out_top_3)
		output_to_file(out_top_3)


# Print and write to file most popular authors
def the_most_popular_authors():
	most_popular_authors = db_query(popular_authors)
	title = "Most Popular Authors"
	print_title(title)
	output_to_file('\n' + title + '\n')
	for name, num in most_popular_authors:
		top_authors = (" {0} -- {1} views".format(name, num))
		print(top_authors)
		output_to_file(top_authors)


# Print and write to file the days that more than 1% requests lead to errors
def days_errors_display():
	days_error = db_query(error_days)
	title = "The days that more than 1% requests lead to errors is"
	print_title(title)
	output_to_file('\n' + title + '\n')
	for days, error_percentage in days_error:
		error_day = """{0:%B %d, %Y} -- {1:.3f} % errors""" \
			.format(days, error_percentage)
		print(error_day)
		output_to_file(error_day)


# Main Function (call all the declared functions)
if __name__ == '__main__':
	remove_text_file(text_file)
	top_3_articles()
	the_most_popular_authors()
	days_errors_display()
	print("Please refer to log_analysis.txt for the resulting queries")
