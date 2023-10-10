class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showName(self):
        return self.name
    def showSalary(self):
        return self.salary
    def showIndexedSalary(self):
        self.salary = self.salary * 110 / 100
        return self.salary

firstEmployee = Employee('Andrew', 23222)
print(firstEmployee.showName())
print(firstEmployee.showSalary())
print(firstEmployee.showIndexedSalary())