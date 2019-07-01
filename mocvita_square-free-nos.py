from math import *
from sqarefree import *

n=int(input("enter a number="))
count=0
for i in range(2,n+1):
    if(n%i==0):
        if pow(int(sqrt(i)),2)!=i:
            if squarefree(i)==True:
                count+=1
            else:
                pass
print("no of perfect squares are",count)