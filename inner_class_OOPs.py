class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap = self.laptop()
    def show(self):
        print(self.name,self.roll)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand)
            print(self.cpu)
            print(self.ram)

s1=student("navin",65)
s2=student("pola",78)

s1.show()


