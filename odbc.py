
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="dvdrental",
    user="postgres",
    password="Kurinchi@123")


cur = conn.cursor()

cur.execute("select * from actor")
rows = cur.fetchall()

# for i in rows:
#     print(i)

"""Task : restore dvdrental db into postgres, create 10 new actors in actors 
          table and list actors whose actors id < 10"""

cur .execute("select actor_id from actor where actor_id > 10 ")
for data in cur:
    print(data)