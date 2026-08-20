#Q21 — Nested Dictionary: Highest Salary
employees = {
    "E001": {
        "name": "Ali",
        "salary": 75000
    },

    "E002": {
        "name": "Sara",
        "salary": 85000
    },

    "E003": {
        "name": "Usman",
        "salary": 65000
    },

    "E004": {
        "name": "Hina",
        "salary": 95000
    }
}

highest_salary = 0
highest_employee = ""

for employee_id, employee in employees.items():

    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
        highest_employee = employee["name"]

print("Employee:", highest_employee)
print("Salary:", highest_salary)