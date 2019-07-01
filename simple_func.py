from prime_or_not import *

func=10
x=int(input("enter the value of x="))
if x<=1:
    func=1
elif(x>1):
    i=2
    while i<x:
        if x%(i*i)==0:
            func=0
            break
        i+=1
else:
    c=0
    fact=1
    for i in range(2,x):
        if(x%i==0):
            if prime(i):
                fact=fact*i
    if fact==x:
        func=1
    else:
        func=-1
print(func)


