from numpy import *

arr=array([3,4,6,7,8])
arr2=array([5,6,7,8,5])
ar=arr+arr2

arr=arr+5

print(arr)
print(ar)
print(sin(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))
print(concatenate([arr,arr2]))

arr=arr2
print(arr)

print(id(arr))
print(id(arr2))

a=array([3,4,5,6,7])
a1=array([2,3,8,9])
a=a1.view()
print(a)
print(id(a))
print(id(a1))

