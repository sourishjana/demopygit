a=5
b=0
try:
    print("open resource")
    print(a/b)
except ZeroDivisionError as e:
    print("wrong,cannot divide by zero",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("something went wrong...",e)
finally:
    print("resorce closed")
print("bye")