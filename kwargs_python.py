

def person(name,*data):

    print(name)
    print(data)


person("navin",28,"mumbai",746289289)


def person(name, **data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)


person("navin", age=28, city="mumbai", phn=746289289)