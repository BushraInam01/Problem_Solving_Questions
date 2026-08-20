#Q14 - Find Duplicate Employee IDs

employee_ids = [101, 102, 103, 101, 104, 105, 102]

duplicates = []

for employee_id in employee_ids:

    if employee_ids.count(employee_id) > 1:

        if employee_id not in duplicates:
            duplicates.append(employee_id)

print("Duplicate IDs:", duplicates)