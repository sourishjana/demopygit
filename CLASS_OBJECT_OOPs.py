
class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("configuration is=",self.cpu,self.ram)

com1=computer('i5',16)
com2=computer('ryzen',8)

com1.config()
com2.config()


print("------------------defining class--------------------")
print(type(com1))
a=5
print(type(a))
b='pola'
print(type(b))