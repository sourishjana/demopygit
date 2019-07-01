from numpy import *

arr=array([
            [2,3,4,7,8,9],
            [5,7,9,3,2,7]
            ])
print(arr[1][1])
arr2=arr.flatten()

arr3=arr2.reshape(3,4)

arr4=arr2.reshape(2,2,3)

print(arr4)
print(arr3)
print(arr2)
print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

a=array([[2,3,4],[4,5,6]])

m=matrix(a)
m1=matrix('1 2 3 ;4 5 6 ;7 9 8')
m2=matrix('1 7 3 ;4 3 6 ;5 9 8')


print(m1)
print(m)
print(diagonal(m1))
print(m1.min())
print(m1.max())


m3=m1+m2
print(m3)

m3=m1*m2
print(m3)