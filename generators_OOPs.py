def topten():
    yield 1
    yield 2
    yield 3
    yield 4


val=topten()
print(val.__next__())
print(val.__next__())

print("-----------top ten perfect squares------------------")

def topten():
    n=1
    while n<=10:
        p=n*n
        yield p
        n+=1
val=topten()
print(val.__next__())
for i in val:
    print(i)
