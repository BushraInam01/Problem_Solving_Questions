#Q12- Find Largest and Smallest Salary List

salaries = [45000, 72000, 38000, 95000, 61000, 52000]

largest = salaries[0]
smallest = salaries[0]

for salary in salaries:

    if salary > largest:
        largest = salary

    if salary < smallest:
        smallest = salary

print("Largest Salary: ",largest)
print("Smallest Salary: ",smallest)