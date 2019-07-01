
#x=int(input("enter a number="))
def prime(x):
    count=0
    for i in range(1,x+1):
        if(x%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False
#if prime(x):
    #print("prime")
#else:
    #print("not prime")