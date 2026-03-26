import sqlite3

def show_all_teachers():
    conn = sqlite3.connect('research_data.db')
    cursor = conn.cursor()

    # The SELECT command - The most famous SQL command
    cursor.execute("SELECT * FROM teachers")
    
    # fetchall() grabs every row from the 'Shelves'
    rows = cursor.fetchall()
    
    print("--- REGISTERED TEACHERS ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[2]} | Score: {row[5]}")

    conn.close()

if __name__ == "__main__":
    show_all_teachers()