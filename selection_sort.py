def sort(list):
    for i in range(len(list)-1):
        min=i
        for j in range(i,len(list)):
            if list[j]<list[min]:
                min=j
            temp=list[min]
            list[min]=list[i]
            list[i]=temp
            print(list)
list=[5,6,7,8,3,4,2]
sort(list)
print(list)