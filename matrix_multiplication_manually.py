from numpy import *

arr1=array([[0,0,0],[0,0,0],[0,0,0]])
arr2=array([[0,0,0],[0,0,0],[0,0,0]])
result=array([[0,0,0],[0,0,0],[0,0,0]])



for i in range(len(arr1)):
    for j in range (len(arr2[0])):
        for k in range(len(arr2)):
            result[i][j]+=arr1[i][j]*arr2[i][j]

for r in result:
    print(r)



