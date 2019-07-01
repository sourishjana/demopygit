
lst=[2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,lst))
print(evens)

doubles=list(map(lambda n:n*2,evens))
print(doubles)

from functools import *

sum=reduce(lambda a,b:a+b,doubles)
print(sum)