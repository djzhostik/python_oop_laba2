class User:
    def setYear(self,year):
        self.year = year
    def getYear(self):
        return self.year
class Employee(User):
    def setSalary(self, salary):
        self.salary = salary
    def setName(self, name):
            self.name = name
    def setSurname(self, surname):
        self.surname = surname
    def getSalary(self):
        return self.salary
    def getName(self,):
        return self.name
    def getSurname(self):
        return self.surname
employee = Employee()
employee.setYear('1991')
employee.setSalary('19350')
print(employee.getYear())
print(employee.getSalary())