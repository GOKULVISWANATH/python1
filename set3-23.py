x=[]
y=int(input(""))
if(1<=y<=100000):
    print(y)
    for i in range(1,y+1):
        z=int(input(""))
        x.append(z)
    print(x)
    r=x[-1]
    s=x[-1]
    for i in x:
        if(r>1):
            r=1
    print(r)
else:
    print(0)
