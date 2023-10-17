class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

class Employee(User):
    def setName(self, name):
        if len(name) > 0:
            super().setName(name)
employee = Employee()
employee.setName("John")
print(employee.name)
