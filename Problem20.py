#Q20 — Nested Dictionary: Employee Information
employees = {
    "E001": {
        "name": "Ali",
        "department": "IT",
        "salary": 75000
    },

    "E002": {
        "name": "Sara",
        "department": "HR",
        "salary": 55000
    },

    "E003": {
        "name": "Usman",
        "department": "IT",
        "salary": 90000
    }
}

for employee_id, employee in employees.items():

    if employee["salary"] > 60000:
        print(employee["name"])