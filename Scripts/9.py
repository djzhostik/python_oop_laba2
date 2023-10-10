class Student:
    name = None
    surname = None

    def show(self):
        print(self.name)
        print(self.surname)

firstStudent = Student()
firstStudent.name = 'John'
firstStudent.surname = 'Cameron'
firstStudent.show()