class Employee:
    __name = None
    __age = None
    __salary = None

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        if (age > 0) and (age < 120):
            self.__age = age
        else:
            raise Exception('name is incorrect')
    def setSalary(self, salary):
        self.__salary = salary
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getSalary(self):
        return self.__salary + '$'
employee = Employee('Joe', 91, '1900000')
employee.setName('Bob')
employee.setAge(116)
employee.setSalary('1219291')
print(employee.getName())
print(employee.getAge())
print(employee.getSalary())
