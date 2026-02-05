import sqlite3

conn = sqlite3.connect("subjects.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lectures INTEGER,
    practices INTEGER,
    exams INTEGER
)
""")


cursor.execute("""
INSERT INTO subjects (name, lectures, practices, exams)
VALUES ('Python', 20, 15, 2)
""")

cursor.execute("""
INSERT INTO subjects (name, lectures, practices, exams)
VALUES ('Математика', 18, 8, 3)
""")

cursor.execute("""
INSERT INTO subjects (name, lectures, practices, exams)
VALUES ('Бази даних', 16, 12, 1)
""")

cursor.execute("""
UPDATE subjects
SET practices = 17
WHERE name = 'Python'
""")

conn.commit()


print("Всі предмети:")
cursor.execute("SELECT * FROM subjects")
all_subjects = cursor.fetchall()

for subject in all_subjects:
    print(subject)


print("\nПредмети з лекціями > 15:")
cursor.execute("""
SELECT name, lectures
FROM subjects
WHERE lectures > 15
""")

for row in cursor.fetchall():
    print(row)


print("\nПредмети з практичними > 10:")
cursor.execute("""
SELECT name, practices
FROM subjects
WHERE practices > 10
""")

for row in cursor.fetchall():
    print(row)


print("\nПредмет з найбільшою кількістю екзаменів:")
cursor.execute("""
SELECT name, exams
FROM subjects
ORDER BY exams DESC
LIMIT 1
""")

result = cursor.fetchone()
print(result)

conn.close()