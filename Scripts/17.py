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
        self.age = age
    def setSalary(self, salary):
        self.__salary = salary
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getSalary(self):
        return self.__salary
employee = Employee('Joe', 91, 1900000)
employee.setName('Bob')
employee.setAge(111)
employee.setSalary(1219291)
print(employee.getName())
print(employee.getAge())
print(employee.getSalary())