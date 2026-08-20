#Q17 — Employee Salary Search "Dictionary"

employees = {
    "Ali": 50000,
    "Sara": 65000,
    "Usman": 70000,
    "Hina": 55000
}

name = "Usman"

if name in employees:
    print("Salary:", employees[name])
else:
    print("Employee not found")