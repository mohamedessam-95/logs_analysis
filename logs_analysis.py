import psycopg2

db = psycopg2.connect("dbname=news")
cursor = db.cursor()
cursor.execute("select * from question1")
result1 = cursor.fetchall()
print("Q1 : What are the most popular three articles of all time? \n")
print("------------------------------------")
for i,j in result1:
    print("Article's name : "+str(i)+"  ->  Was viewed "+str(j)+" times.")

print("\n \n Q2 : Who are the most popular article authors of all time? \n")
print("------------------------------------")
cursor.execute("select * from question2")
result2 = cursor.fetchall()
for i,j in result2:
    print("Author : "+str(i)+"  ->  his article was viewed "+str(j)+" times.")

print("\n \n Q3 : On which days did more than 1% of requests lead to errors? \n")
print("------------------------------------")
cursor.execute(
	"select sub.time from (select count(log.status)/100 as requests from log) as perc ,"
	"(select date(time) as time,count(status) as num from log where status like '404%' group by time) as sub"
	" having sub.num > perc.requests")


