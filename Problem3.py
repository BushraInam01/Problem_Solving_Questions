#Q3- Count Digits

number = int(input("Enter a Number: "))
count = 0

while number >0:
    number = number //10
    count = count +1

print("Total Digits: ", count)