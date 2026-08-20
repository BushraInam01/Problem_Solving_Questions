#Q23 - Employee Polymorphism
class Employee:

    def work(self):
        print("Employee is working")


class Developer(Employee):

    def work(self):
        print("Developer writes code")


class Designer(Employee):

    def work(self):
        print("Designer creates UI")


employees = [
    Developer(),
    Designer()
]

for employee in employees:
    employee.work()