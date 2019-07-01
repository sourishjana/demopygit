from array import *

arr=array('i',[])

n=int(input("enter the length of array="))
for i in range(n):
    x=int(input("enter the elements="))
    arr.append(x)

print(arr)

val=int(input("enter the length of array="))
k=0
for e in arr:
    if(val==e):
        print(k)
        break
    k+=1

print(arr.index(val))