class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary


class EmployeesCollection:
    __employees = None

    def __init__(self):
        self.__employees = []

    def add(self, employee):
        self.__employees.append(employee)

    def show(self):
        for employee in self.__employees:
            print(employee.getName())

    def sumSalary(self):
        sum = 0
        for employee in self.__employees:
            salary = employee.getSalary()
            sum += salary
        print(sum)
        return sum

    def avgSalary(self):
        total_sum = self.sumSalary()
        employee_count = len(self.__employees)
        avg_salary = total_sum / employee_count
        print(avg_salary)
        return avg_salary


ec = EmployeesCollection()
ec.add(Employee('john', 22222))
ec.add(Employee('eric', 33333))
ec.add(Employee('kyle', 44444))
ec.show()
ec.sumSalary()
ec.avgSalary()