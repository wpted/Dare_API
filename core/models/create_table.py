import sqlite3

connection = sqlite3.connect("dares.db")
cursor = connection.cursor()

dare_table_creation_query = "CREATE TABLE IF NOT EXISTS dares(" \
                            "dare_id INTEGER PRIMARY KEY," \
                            "dares STRING(550) NOT NULL)"

cursor.execute(dare_table_creation_query)
connection.commit()
connection.close()

