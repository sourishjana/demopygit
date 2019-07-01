
b=4
a=10
print(id(a))
def pola():
    a=15
    c=4
    print("in function",a,b)

def lola():
    global b
    print("in 2nd function",b)

lola()
pola()
print("outside function",a)

def loka():
    x=globals()['a']
    print(id(x))
    print(x)
    globals()['a']=1
    print(a)
loka()
print(a)