import sqlite3 as sql

x = sql.xnect('db_web.db')

curs = x.cursor()

curs.execute("DROP TABLE IF EXISTS users")

sql ='''CREATE TABLE "users" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Firstname"	TEXT,
    "Lastname" TEXT,
    "Age" INTEGER,
    "Gender" TEXT
)'''
curs.execute(sql)

x.commit()

x.close()