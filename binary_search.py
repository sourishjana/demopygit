pos=-1
def binsearch(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        elif list[mid]<n:
            l=mid+1
        else:
            u=mid-1
    return False
list=[2,5,6,7,8,9]
n=6
if binsearch(list,n):
    print("found at",pos+1)
else:
    print("not found")
