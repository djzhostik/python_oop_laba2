class User:
    def setName(self, name):
        self._name = name

    def setSurname(self, name):
            self.surname = surname

    def getName(self):
        return self._name

    def getSurname(self, name):
        return self._surname

class Employee(User):
    def setAge(self, age):
        self._age = age

    def getAge(self):
        return self._age


class Programmer(Employee):
    def setExperience(self, experience):
        self._experience = experience

    def getExperience(self):
        return self._experience

class Designer(Employee):
    def setSkill(self, skill):
        self._skill = skill

    def getSkill(self):
        return self._skill
designer = Designer()
designer.setSkill('draw')
print(designer.getSkill())