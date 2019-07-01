def update(x):
    x=8
    print("x",x)

update(10)
a=10
update(a)
print("a",a)

def update1(x):
    print(id(x),"x")
    x=8
    print(id(x),"updated x")
    print("x",x)
print(id(a),"a")
update1(a)

def update2(list):
    print(id(list))
    list[1]=25
    print(id(list))
    print("x",list)

lst=[10,35,67]
print(id(lst))
update2(lst)
print("list",lst)
