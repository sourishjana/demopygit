from math import *
def squares(n):
    for i in range(2,n+1):
        if(n%i==0):
            if pow(int(sqrt(i)), 2) != i:
                print(i)
def squarefree(n):
    count=0
    c=0
    for i in range(2,n+1):
        if(n%i==0):
            if pow(int(sqrt(i)), 2) == i:
                count=1
    if(count==1):
        return False
    else:
        return True
