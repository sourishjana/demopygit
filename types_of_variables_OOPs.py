

class car:
    wheels=4
    def __init__(self):
        self.milage=10
        self.com="bmw"
c1=car()
c2=car()
c1.milage=8
car.milage=8
car.wheels=3
print(c1.com,c1.milage,c1.wheels)
print(c2.com,c2.milage,c2.wheels)