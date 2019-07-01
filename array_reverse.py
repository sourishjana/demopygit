from array import *
arr=array('i',[])
n=int(input("enter the no of elements="))
for i in range(n):
    x = int(input("enter elements="))
    arr.append(x)
print(arr)
i=0
j=n-1
while(i<j):
    t=arr[j]
    arr[j]=arr[i]
    arr[i]=t
    i+=1
    j-=1
for i in range(n):
    print(arr[i])