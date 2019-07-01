
def greet():
    print("hello","good morning")

greet()
greet()
def add(x,y):
    c=x+y
    print(c)

add(3,4)
def add(x,y):
    c=x+y
    return c
print(add(2,4))

def add_sub(x,y):
    return(x+y),(x-y)

result1,result2=add_sub(3,4)
print(result1)
print(result2)