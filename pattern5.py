s="ABCD"
b="PQR"
for i in range(4):
    for j in range(i+1):
        print(s[j],end="")
    for k in range(i,3):
        print(b[k],end="")
    print()