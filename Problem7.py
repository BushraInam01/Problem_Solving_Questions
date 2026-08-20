#Q7 — Sum of Digits
def sum_of_digits(number):
    number = abs(number)
    total = 0

    while number >0:
        digit = number % 10
        total = total + digit
        number = number //10

    return total

number = int(input("Enter a Number: "))
result = sum_of_digits(number)
print("Sum of Digit Number: ", result)