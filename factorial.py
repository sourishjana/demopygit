n=int(input("enter a number="))
def f(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact
result=f(n)

print(result)