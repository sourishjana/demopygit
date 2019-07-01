
class student:
    school="polaa"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is student class in abc factorial")



s1=student(2,4,5)
s2=student(56,4,6)

print(s1.avg())
print(s2.avg())

print(s1.get_m1())
s1.set_m1(43)
print(s1.get_m1())
print(student.getschool())
student.info()