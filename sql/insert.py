import sqlite3

def insert_student(name: str, grade: float):
    """
    Inserts a new student into the students table.

    Args:
    name (str): The name of the student.
    grade (float): The grade of the student.
    """
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Create the students table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade REAL NOT NULL
    )
    ''')

    # Insert the new student into the students table
    cursor.execute('''
    INSERT INTO students (name, grade)
    VALUES (?, ?)
    ''', (name, grade))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

