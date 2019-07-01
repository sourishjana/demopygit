from array import *

a=array('i',[2,4,5,7,1])

max=a[0]

for i in range(1,len(a)):
    if(a[i]>max):
        max=a[i]

print(max)