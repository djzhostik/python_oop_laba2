class User:
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age
class Employee(User):
    def setAge(self,age):
        if (age > 18) and (age < 65):
            self.age = age
        else:
            raise Exception("age is incorrect!")
employee = Employee()
employee.setAge(66)
print(employee.getAge())