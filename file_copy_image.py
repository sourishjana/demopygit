f=open('PASPORT CROP.jpg','rb')

for data in f:
    print(data)
#fetching all the data from the image file

f1=open('pasport_copy.jpg','wb')

for data in f:
    f1.write(data)

#but unfortunately due to format problem the pic cannot be loaded