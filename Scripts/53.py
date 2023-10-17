class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def getArea(self):
        return 3.14*self.__radius*self.__radius
    def getCircumference(self):
        return 2 * 3.14 * self.__radius
circle = Circle(1)
print(circle.getArea())
print(circle.getCircumference())
