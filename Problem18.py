#Q18 — Count Employees by Department
employees = {
    "Ali": "IT",
    "Sara": "HR",
    "Usman": "IT",
    "Hina": "Marketing",
    "Ahmed": "IT",
    "Ayesha": "HR"
}

department_count = {}

for name, department in employees.items():

    if department not in department_count:
        department_count[department] = 1
    else:
        department_count[department] += 1

print(department_count)