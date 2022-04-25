

students = [
    ('Bob', 95),
    ('Tina', 97),
    ('John', 86),
    ('Sri', 90),
    ('London', 80),
    ('Lyndon', 101)
]

for student in students:
    if student[0] == 'Tina':
        students.remove(student)


for student in students:
    print(student)