import sqlite3
import os

def create_database():
    """
    Creates the 'school.db' database, sets up the table schema, 
    and inserts the sample data as required by the assignment.
    """
    
    # Check if file exists and remove it to ensure a fresh start
    db_file = 'school.db'
    if os.path.exists(db_file):
        os.remove(db_file)

    # 1. Create a New Database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # 2. Create Tables
    
    # Table 1: students
    cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        full_name TEXT,
        birth_year INTEGER
    )
    ''')

    # Table 2: grades
    cursor.execute('''
    CREATE TABLE grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject TEXT,
        grade INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
    ''')

    # 3. Insert Sample Data
    
    # 3.1 Students Data
    students_data = [
        ('Alice Johnson', 2005),
        ('Brian Smith', 2004),
        ('Carla Reyes', 2006),
        ('Daniel Kim', 2005),
        ('Eva Thompson', 2003),
        ('Felix Nguyen', 2007),
        ('Grace Patel', 2005),
        ('Henry Lopez', 2004),
        ('Isabella Martinez', 2006)
    ]
    
    cursor.executemany("INSERT INTO students (full_name, birth_year) VALUES (?, ?)", students_data)

    # 3.2 Grades Data
    # Assuming IDs are generated sequentially from 1 to 9 based on the insertion order above.
    grades_data = [
        (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
        (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
        (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
        (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
        (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
        (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
        (7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
        (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
        (9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92)
    ]

    cursor.executemany("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", grades_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database 'school.db' created and populated successfully.")

if __name__ == "__main__":
    create_database()
