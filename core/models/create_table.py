import sqlite3
from core.util.get_dares import question_list

connection = sqlite3.connect("dares.db")
cursor = connection.cursor()

dare_table_creation_query = "CREATE TABLE IF NOT EXISTS dares(" \
                            "dare_id INTEGER PRIMARY KEY," \
                            "dares STRING(550) NOT NULL)"

cursor.execute(dare_table_creation_query)

for question in question_list:
    insert_query = "INSERT INTO dares VALUES (NULL, ?)"
    cursor.execute(insert_query, (question,))

connection.commit()
connection.close()
