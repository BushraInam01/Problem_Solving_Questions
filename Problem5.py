#Q5 — Even/Odd Using Function

def check_even_odd(number):
    if number %2 ==0:
        return "even"
    else:
        return "odd"

number = int(input("Enter a Number: "))
result = check_even_odd(number)

print("Result: ", result)