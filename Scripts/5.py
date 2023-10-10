class Employee:
    age = None
    def show(self, age):
        return age
firstEmployee = Employee()
c = firstEmployee.show(34)
print(c)