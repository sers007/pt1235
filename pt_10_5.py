import sqlite3


connection = sqlite3.connect("p10 test.sl3", 5)
cur = connection.cursor()
cur.execute("DELETE FROM first_table WHERE rowid=5 ")
connection.commit()
connection.close()
