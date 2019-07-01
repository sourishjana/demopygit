x=5
y=98
z=x+y
print(z)

import numpy as np #clockwise,anticlockwise rotation of matrix
#n=int(input("Number of Rows of the Square Matrix:"))
arr=[]
print("Enter elements of Matrix:")
for i in range(4):
    l=list(map(int,input().split(",")))
    arr.append(l)
print("The given Matrix is:")
for i in range(2):
    for j in range(2):
        print(arr[i][j],end=" ")
    print()