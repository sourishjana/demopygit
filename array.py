from array import *
import array as a

val=array('i',[5,6,7,-8,9,3])
print(val[0])
val.reverse()
print(val)

val.append(7)
print(val)

print(val[0])

for i in range(len(val)):
    print(val[i],end="")
print()

for i in val:
    print(i,end="")
print()

i=0
while(i<len(val)):
    print(val[i],end="")
    i+=1
print()

newarr=array(val.typecode,(i for i in val))

newarr=array(val.typecode,(i*i for i in val))

for i in newarr:
    print(i,end="")
print()


ch=array('u',['a','j','k','y','r'])

for i in ch:
    print(i,end="")
print()

print(val.buffer_info())