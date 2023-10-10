class Student:
    name = None
    surname = None

    def show(self):
        return self.cape(self.name + ' ' + self.surname)
    def cape(self,str):
        return str.title()
    def initials(self,str):
        return self.name[0].title() + '.' + self.surname[0].title() + '.'

firstStudent = Student()
firstStudent.name = 'joe'
firstStudent.surname = 'clark'
print(firstStudent.show())
print(firstStudent.initials(firstStudent.surname))

