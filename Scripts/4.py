class Employee:
    name = None
    salary = None
    def output(self):
        print(self.name)
        print(self.salary)
firstEmployee = Employee()
secondEmployee = Employee()
firstEmployee.name = 'Joe'
firstEmployee.salary = 30000
secondEmployee.name = 'John'
secondEmployee.salary = 44444
firstEmployee.output()
secondEmployee.output()