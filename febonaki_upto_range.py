def fib(n):
    c=0
    a = 0
    b = 1
    while(a<=n):
        print(a)
        c = a + b
        a=b
        b=c

n=int(input("enter the range="))
fib(n)