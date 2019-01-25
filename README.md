# Logs Analysis Project
The scope is to build informative summary from logs by using sql database queries. The summary interacts with a live database both from the command line and from the python code. This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

## Technologies used
1. PostgreSQL
2. Writing Python code with DB-API
3. Vagrant - Linux-based virtual machine (VM) 

## Project Requirements
The tool will have to report & answer three questions below.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

* Project follows good SQL coding practices: Each question should be answered with a single database query.  
* The code is error free and conforms to the PEP8 style recommendations.
* The code presents its output in clearly formatted plain text.

## System setup and how to view this project
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.
1. Install [Vagrant](https://www.vagrantup.com/).
2. Install [Virtual Box](https://www.virtualbox.org/). 
3. Clone this repository.
4. Download the **newsdata.sql** (extract from **newsdata.zip** ([here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip))) and **log_analysis.py** files from the respository and move them to your **vagrant** directory within your VM.

#### Run these commands from the terminal in the folder where your vagrant is installed in: 
1. ```vagrant up``` to boot up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```cd Log-Analysis``` to switch to the working reporting tool directory
6. ```python3 log_analysis.py``` to run the reporting tool.

## Additional view queries used
#### status_total
````sql
CREATE VIEW status_total AS
SELECT time ::date,
       status
FROM log;
````
#### failed_status
````sql
CREATE VIEW failed_status AS
SELECT time,
       count(*) AS num
FROM status_total
WHERE status = '404 NOT FOUND'
GROUP BY time;
````
#### all_status
````sql
CREATE VIEW all_status AS
SELECT time, 
       count(*) AS num
FROM status_total
WHERE status = '404 NOT FOUND'
  OR status = '200 OK'
GROUP BY time;
````
#### percentage_total
````sql
CREATE VIEW percentage_total AS
SELECT all_status.time,
       all_status.num AS total,
       failed_status.num AS failure_rate,
       failed_status.num::real /all_status.num::real * 100 AS failure_percentage
FROM all_status,
     failed_status, 
WHERE all_status.time = failed_status.time;
````

## Helpful Resources
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [W3School - Create View in SQL](https://www.w3schools.com/sql/sql_view.asp)
* [W3School - Substring](https://www.w3schools.com/sql/func_mysql_substr.asp)
* [Python Software Foundation - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Github Gist - SQL Cheat Sheet](https://gist.github.com/janikvonrotz/6e27788f662fcdbba3fb)