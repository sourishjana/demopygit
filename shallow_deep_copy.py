from numpy import *

print("shallow copy")

arr1=array([2,4,5,6,7])
arr2=array([4,5,6,7])

arr1=arr2.view()

arr2[1]=8

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

print("deep_copy")

a1=array([2,4,5,7,8])
a2=array([4,6,9,2,1])
a1=a2.copy()
a2[1]=8

print(a1)
print(a2)

print(id(a1))
print(id(a2))
