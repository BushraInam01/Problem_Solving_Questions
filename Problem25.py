#Q25 — Find Students Who Scored 80 or Above
students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 67},
    {"name": "Ahmed", "marks": 92},
    {"name": "Ayesha", "marks": 74},
    {"name": "Usman", "marks": 55},
    {"name": "Hina", "marks": 88}
]

for student in students:
    if student["marks"] >= 80:
        print(student["name"])