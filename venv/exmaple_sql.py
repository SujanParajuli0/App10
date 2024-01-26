import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("/Users/sujanparajuli/PycharmProjects/App10/data.db")
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE band='Tiger'")
rows = cursor.fetchall()
print(rows)

# Query certain columns data
cursor.execute("SELECT band, date FROM events WHERE band='Tiger'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Cats', 'Cat City', '2023.12.17'),
            ('Hens', 'Hens City', '2023.12.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)