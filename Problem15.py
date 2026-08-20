#Q15 - Search Employee by ID
employee_ids = [101, 102, 103, 104, 105]

search_id = int(input("Enter Employee ID: "))

found = False

for employee_id in employee_ids:

    if employee_id == search_id:
        found = True
        break

if found:
    print("Employee Found")
else:
    print("Employee Not Found")