#Q13 - Find Employees Who Earn Above Average

salaries = [40000, 55000, 60000, 75000, 90000]
total = 0

for salary in salaries:
    total +=salary

averge = total / len(salaries)

print("Average Salary:", averge)

print("Salaries above average:")

for salary in salaries:
    if salary > averge:
        print(salary)