class Employee:
    name = None
    salary = None
    def showName(self):
        print(self.name)
    def showSalary(self):
        print(self.salary)
newEmployee = Employee()
newEmployee.name = 'Joe'
newEmployee.salary = 30000
newEmployee.showName()
newEmployee.showSalary()