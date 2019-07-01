class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def show(self):
        print(self.name)
        print(self.roll)
    class laptop:
        weight=34
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram
        def show(self):
            print(self.brand)
            print(self.cpu)
            print(self.ram)
        @classmethod
        def getweight(cls):
            return cls.weight

s1=student("navin",65)
s2=student("pola",78)

s1.show()

lap1=student.laptop('hp','i5',16)
lap1.show()
print(student.laptop.getweight())