class Rectangle:
    def __init__(self, height, weight):
        self.__height = height
        self.__weight = weight
    def getSquare(self):
        return self.__weight*self.__height
    def getPerimeter(self):
        return (self.__weight + self.__height) * 2
    def getRatio(self):
        return (self.__weight * self.__height) / ((self.__weight + self.__height) * 2 )

rectangle = Rectangle(11, 5)
print(rectangle.getSquare())
print(rectangle.getPerimeter())
print(rectangle.getRatio())
