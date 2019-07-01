

class computer:
    def __init__(self):
        self.name="navin"
        self.age=28
    def update(self):
        self.age=30
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=computer()
c2=computer()

c1.name="pola"
c1.age=19
c1.update()

if c1.compare(c2):
    print("they are same")
else:
    print("not same")

print(c1.name)
print(c2.name)
print(c1.age)