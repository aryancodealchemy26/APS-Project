import sqlite3

def init_db():
    # Connect to (or create) a file called research_data.db
    conn = sqlite3.connect('research_data.db')
    cursor = conn.cursor()

    # CREATE TABLE is a Data Definition Language (DDL) command
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            first_name TEXT,
            locality TEXT,
            subject TEXT,
            readiness_score INTEGER,
            gender TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Run this once to setup the lab
if __name__ == "__main__":
    init_db()
    print("Database and Table created successfully!")

def save_teacher_result(email, name, locality, subject, score,gender):
    # Connect to the DB file
    conn = sqlite3.connect('research_data.db')
    cursor = conn.cursor()

    # The INSERT INTO command (Data Manipulation Language - DML)
    # We use '?' placeholders to prevent SQL INJECTION (Security Concept)
    query = '''
        INSERT INTO teachers (email, first_name, locality, subject, readiness_score,gender)
        VALUES (?, ?, ?, ?, ?,?)
    '''
    
    try:
        cursor.execute(query, (email, name, locality, subject, score,gender))
        conn.commit()
        print(f"Data for {name} saved successfully!")
    except sqlite3.IntegrityError:
        print("Error: This email already exists in the database.")
    
    conn.close()