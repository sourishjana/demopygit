n=20
for i in range (0,n):
    if i<=1:
        for j in range(0,i+1):
            print("*",end="")
    elif(i<=4):
        for j in range(0,i*2):
            print("*",end="")
    else:
        for j in range(0,i*2-1):
            print("*",end="")
    print()
