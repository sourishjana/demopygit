from array import *
arr=array('i',[3,7,5,2,9])

for i in range(5-1):
    for j in range(5-i-1):
        if(arr[j]>arr[j+1]):
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=arr[j]

for i in arr:
    print(i)