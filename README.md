# Logs Analysis Project

This project answers these three questions by querying their answers from a database :

1) What are the most popular three articles of all time ?
2) Who are the most popular article authors of all time ?
3) On which days did more than 1% of requests lead to errors ?

The Output lines of the python file are found in the Outputs.txt file

# Setup
## Software
You need this software installed on your computer.

Python 3 :(https://www.python.org/downloads/)

PostgreSQL : (https://www.postgresql.org/download/)

## Test data
You need to download and extract the database from udacity called newsdata.sql and build it inside your environment using this code in the bash window ```psql -d news -f newsdata.sql``` hence it is a PostGreSQL Database

## Views
This project rely totally on views so you must recreate them first in order for the system to be in place , Each question is answered in by a separate view , and you can find the code to create these views below ...

### For the Question "What are the most popular three articles of all time?"
```
create view question1 AS select articles.title, count(*) as num from articles join log on articles.slug = substr(log.path, 10) where path != '/' group by articles.title order by num desc limit 3;
```

### For the Question "Who are the most popular article authors of all time?"
```
create view question2 AS select authors.name, sub.num from authors join (select articles.author, count(*) as num from articles join log on articles.slug = substr(log.path, 10) where path != '/' group by articles.author order by num desc) as sub on sub.author = authors.id;
```

### For the Question "On which days did more than 1% of requests lead to errors?"
```
create view question3 AS with errors as (select time, count(*) as error_num from (select date(time) as time ,status from log where status like '404%') as filtered group by time), total as (select date(time) as time ,count(*) as total_num from log group by date(time)) select time, percent from (select total.time, cast(error_num as decimal)/cast(total_num as decimal) as percent from errors join total on errors.time = total.time) as sub where percent > 0.01
```

# How to run the application

After you have successfully installed the required software , built the database and recreated the views you can simply run the application by typing this line in your shell like if you are using vagrant : ``` python logs_analysis.py ``` but make sure that your current directory is the one containing the logs_analysis.py file

