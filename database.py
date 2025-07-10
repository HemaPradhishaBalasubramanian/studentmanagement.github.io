import sqlite3

def connect():
    global conn, cursor
    conn = sqlite3.connect("students.db", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    """)
    conn.commit()


def insert(name, age, course):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
def fetch_all():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


def search(name):
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    return cursor.fetchall()

def delete(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

def update(student_id, name, age, course):
    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, student_id))
    conn.commit()

