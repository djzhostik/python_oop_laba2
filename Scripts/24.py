class Employee :
    name = None
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def getName(self):
        return self.name, self.salary
employees = [
	 Employee('john','32000'),
	 Employee('eric','27000'),
	 Employee('kyle','19000'),
]
for employee in employees:
    print(f"{employee.name}")
    print(f"{employee.salary}")