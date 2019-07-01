print("---------file reading--------")
f=open('mydata','r')

for data in f:
    print(data,end="")
#printing one single line
print(f.readline())#to implement this line omit the upper for loop

