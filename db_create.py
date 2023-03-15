import sqlite3 as sql
import csv


# connect to SQLite
con = sql.connect('database.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS earthquake")

#Create users table  in db_web database
sql ='''CREATE TABLE "earthquake" (
	"time"	TEXT,
	"latitude"	REAL,
    "longitutde" REAL,
    "depth" REAL,
    "mag" REAL,
    "magType" TEXT,
    "nst" INTEGER,
    "gap" REAL,
    "dmin" REAL,
    "rms" REAL,
    "net" TEXT,
    "id" TEXT,
    "updated" TEXT,
    "place" TEXT,
    "type" TEXT,
    "horizontalError" REAL,
    "depthError" REAL,
    "magError" REAL,
    "magNst" INTEGER,
    "status" TEXT,
    "locationSource" TEXT,
    "magSource" TEXT
)'''
cur.execute(sql)

a_file = open("static/all_month.csv",encoding='utf8')
rows = csv.reader(a_file)
print(rows)
cur.executemany("INSERT INTO earthquake VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)

#commit changes
con.commit()

#close the connection
con.close()