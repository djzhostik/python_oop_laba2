class User:
    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department
class Position :
    city = None
    def __init__(self,name):
        self.name = name

class Department:
    department = None
    def __init__(self, name):
        self.name = name
position = Position("программист")
department = Department("отдел ИТ")
user = User("Иван", position, department)
print (user.name)
print(user.position.name)
print(user.department.name)

