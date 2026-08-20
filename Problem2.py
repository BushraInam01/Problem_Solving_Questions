#Q2 — Reverse an Integer
def reverse_number(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return reverse


number = int(input("Enter a number: "))

result = reverse_number(number)

print("Reverse Number: ", result)