import sqlite3

conn = sqlite3.connect('research_data.db')
cursor = conn.cursor()

# Adding a new column without deleting existing data
try:
    cursor.execute("ALTER TABLE teachers ADD COLUMN gender TEXT")
    conn.commit()
    print("Database Schema Updated: Added 'gender' column.")
except sqlite3.OperationalError:
    print("Column already exists!")

conn.close()