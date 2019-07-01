def sum(x,y):
    c=x+y
    print(c)

sum(5,6)
print("position")
def person(name,age):
    print(name)
    print(age)

person('navin',28)
print("keyword")
person(age=28,name="navin")
print("default")
def person(name,age=18):
    print(name)
    print(age)

person("navin")

print("variable length")
def sum(x,*y):
    c=x
    for i in y:
        c=c+i
    print(c)

sum(4,5,7,8)
def sum(*y):
    c=0
    for i in y:
        c=c+i
    print(c)

sum(4,5,7,8)