class Employee:
	def show(self, name, salary):
		return name + ' ' + salary
firstEmployee = Employee()
c = firstEmployee.show('Joe', '32000')
print(c)