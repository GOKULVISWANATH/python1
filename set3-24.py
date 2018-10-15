x=[]
y=int(input("value:"))
if(1<=y<=1000):
    for i in range(y):
        y=int(input("list:"))
        x.append(y)
        print(sorted(x))
else:
    print(0)
