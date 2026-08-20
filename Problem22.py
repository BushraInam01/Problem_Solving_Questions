#Q22 — Nested Dictionary: Department + Employees + Salary
company = {
    "IT": {
        "Ali": 80000,
        "Usman": 90000,
        "Ahmed": 70000
    },

    "HR": {
        "Sara": 60000,
        "Hina": 65000
    },

    "Marketing": {
        "Ayesha": 55000,
        "Zara": 75000
    }
}

for department, employees in company.items():

    total_salary = 0

    for name, salary in employees.items():
        total_salary += salary

    average_salary = total_salary / len(employees)

    print("Department:", department)
    print("Total Salary:", total_salary)
    print("Average Salary:", average_salary)
    print()