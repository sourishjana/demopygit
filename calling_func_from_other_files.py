from calc import *

a,b=2,9

c=add(a,b)
print(c)
def smart_sub(func):
    def inner (a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner
div=smart_sub(div)
c=div(a,b)
print(c)
c=multiply(a,b)
print(c)