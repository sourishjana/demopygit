from math import *
r=int(input("enter the radius="))
h=int(input("enter the height="))
s=int(input("enter the height of bug="))
point=str(input("for which point you want to give input=F or C"))
if(point=='F'):
    a=int(input("enter the distance from toppest point="))
    a=abs(a)
    q=int(input("enter the angle="))
else:
    t = int(input("enter the distance from the point B="))
    p = int(input("enter the angle="))
if point=='F':
    if q==180:
        distance=a+r+s
        print(distance)
    elif q==0:
        distance=r-a+s
        print(distance)
    else:
        print("calculations needed")
else:
    if p==180:
        distance=s+(2*r)+t
        print(distance)
    elif p==0:
        distance=abs(s-t)
        print(distance)
    else:
        base=(p*3.14*r)/180
        perpendicular=abs(s-t)
        hy=sqrt((base*base)+(perpendicular*perpendicular))
        print(hy)
