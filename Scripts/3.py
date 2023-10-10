class Employee:
    name = None
    age = None
    salary = None
    def output(self):
        print(self.name)
        print(self.age)
        print(self.salary)
firstEmployee = Employee()
firstEmployee.name = 'Joe'
firstEmployee.age = 11
firstEmployee.salary = 30000
firstEmployee.output()