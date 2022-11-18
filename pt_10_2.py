import sqlite3


connection = sqlite3.connect("p10 test.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
connection.commit()
connection.close()
