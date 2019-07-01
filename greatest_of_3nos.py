x=int(input("enter 1st number="))
y=int(input("enter 1st number="))
z=int(input("enter 1st number="))
if(x>y):
    if(x>z):
        print("greatest is ",x)
    else:
        print("greatest is ",z)
else:
    if(y>z):
        print("greatest is ",y)
    else:
        print("greatest is ",z)
