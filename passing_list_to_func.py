
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


lst=[3,4,5,6,7,8,9,21,34]


even,odd=count(lst)
print(even)
print(odd)
print("even :{} and odd:{}".format(even,odd))