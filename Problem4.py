#Q4- Palindrome Integer
number = int(input("Enter a Number: "))
reverse = 0
original = number

while number>0:
    digit = number %10
    reverse = reverse * 10 + digit
    number = number //10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")