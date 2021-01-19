import sqlite3

conn = sqlite3.connect('app.db')
print('Database connection opened')

try:
  conn.execute('CREATE TABLE visits (visit_time TEXT)')
except Exception as e:
  print('Table already exists')

conn.close()
