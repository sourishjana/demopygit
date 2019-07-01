nums=[2,3,4,5,7]

print(nums[3])
for i in nums:
    print(i)

print("----------using iterator-------------")
it=iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it))
for i in nums:
    print(i)

print("------------using own class-------------------")

class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=topten()
print(values.__next__())
for i in values:
    print(i)