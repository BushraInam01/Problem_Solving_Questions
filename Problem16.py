#Q16 - Calculate Department Expenses

expenses = {
    "HR": [15000, 20000, 10000],
    "IT": [50000, 35000, 40000],
    "Marketing": [25000, 15000, 20000]
}

for department, amounts in expenses.items():

    total = 0

    for amount in amounts:
        total += amount

    print(department, "Expense:", total)