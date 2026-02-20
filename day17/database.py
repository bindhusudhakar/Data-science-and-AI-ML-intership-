import sqlite3

# Connect (creates database)
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Aisha', 'Data Science', 15000)")
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Rahul', 'Web Dev', 12000)")
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Sneha', 'Machine Learning', 18000)")
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Arjun', 'Data Science', 16000)")
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Meera', 'Web Dev', 11000)")

conn.commit()

# Select specific columns
cursor.execute("SELECT name, track FROM interns")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()