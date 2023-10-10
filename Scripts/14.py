class Employee:
    __name = None
    __salary = None
    def __init__(self,name, salary):
        self.__name = name
        self.__salary = salary

    def getSalary(self):
        return self.addSign(self.__salary)
    def addSign(self,num):
	    return num + '$'

firstEmployee = Employee('Tom', '12992')
print(firstEmployee.getSalary())

