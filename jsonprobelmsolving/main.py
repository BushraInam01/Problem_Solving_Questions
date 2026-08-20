import json

# =========================
# Problem 26
# =========================

with open("Problem26.json", "r") as file:
    data = json.load(file)

for student in data["students"]:
    print(student["name"])


# =========================
# Problem 27
# =========================

with open("Problem27.json", "r") as file:
    data = json.load(file)

for employee in data["employees"]:
    print(employee["name"], "-", employee["salary"])


# =========================
# Problem 28
# =========================

with open("Problem28.json", "r") as file:
    data = json.load(file)

for student in data["students"]:
    print(student["name"], "-", student["address"]["city"])


# =========================
# Problem 29
# =========================

with open("Problem29.json", "r") as file:
    data = json.load(file)

for product in data["products"]:
    if product["price"] > 10000:
        print(product["name"], "-", product["price"])

# =========================
# Problem 30
# =========================

with open("Problem30.json", "r") as file:
    data = json.load(file)

for student in data["students"]:
    if student["marks"] >= 70:
        print(student["name"], "-", student["marks"])