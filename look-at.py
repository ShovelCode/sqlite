import sqlite3

#connect to database
conn = sqlite3.connect('database2.db')

#create cursor
cursor = conn.cursor()

#query the database
cursor.execute('Select * from users')
rows = cursor.fetchall()

#print out
for row in rows:
  print(row)

#close connection
conn.close()
