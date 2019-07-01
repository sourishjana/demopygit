from numpy import *
p=array([['A','S','L','D'],
        ['T','R','W','R'],
        ['R','M','S','R'],
        ['W','R','R','M']])
print(p)
source=p[0][0]
for i in range(4):
    for j in range(4):
        if(p[i][j]=='R'):
            for i in range(i-1,i+2):
                for j in range(j-1,j+2):



