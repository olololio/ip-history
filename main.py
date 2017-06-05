import getMyIP
import os
import sqlite3
import datetime

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

db_filename = 'data-database.db' 
conn = sqlite3.connect(db_filename)
conn.execute('CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY AUTOINCREMENT, time DATETIME, ip VARCHAR(15))')
conn.commit()

time = datetime.datetime.now()
ip = getMyIP.getIPfromHttpBinOrg()

c = conn.cursor()
sql = 'insert into history (time, ip) values (:time, :ip)'
c.execute(sql, (time, ip))
conn.commit()