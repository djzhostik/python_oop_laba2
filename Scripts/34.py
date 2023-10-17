class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.__capeFirst(self.name)

    def __capeFirst(self, stri):
        return stri
class Employee(User):
    def setSurn(self, surname):
        self.surname = surname

    def getSurn(self):
        return self.__capeFirst(self.surname)
employee = Employee()
c = employee.getSurn()
print(c)
##выдаёт ошибку AttributeError: 'Employee' object has no attribute '_Employee__capeFirst'