class Car:
    color = None
    fuel = None
    transmission = None
    seats = None

    def output(self):
        print(self.color)
        print(self.fuel)
        print(self.transmission)
        print(self.seats)

myCar = Car()
myCar.color = 'red'
myCar.fuel = 50
myCar.transmission = 'manual'
myCar.seats = 5

myCar.output()