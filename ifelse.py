x=int(input("enter a number="))
if (x%2):
    print("odd")
    if (x<5):
        print("not great")
    else:
        print("great")
elif (x==0):
    print("zero")
else:
    print("even")