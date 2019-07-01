from array import *
arr=array('i',[])
n=int(input("enter the no of elements="))
for i in range(n):
    x = int(input("enter the elements="))
    arr.append(x)
print(arr)
val=int(input("enter element you want to delete="))
k=arr.index(val)
print(k)
n=n-1
for l in range(k,n):
    arr[l]=arr[l+1]

for i in range(n):
    print( arr[i],end="")