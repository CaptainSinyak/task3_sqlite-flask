import sqlite3 as sql

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
  with sql.connect('app.db') as conn:
    conn.row_factory = sql.Row
    c = conn.cursor()

    c.execute('SELECT * FROM visits')

    rows = c.fetchall()

  return f'Visit count: {len(rows)}'

@app.route('/visit')
def visit():
  with sql.connect('app.db') as conn:
    c = conn.cursor()

    c.execute('INSERT INTO visits (visit_time) VALUES (?)', (str(datetime.now()),))
    conn.commit()

    print('Inserted a new visit')

  return 'Visited!'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
