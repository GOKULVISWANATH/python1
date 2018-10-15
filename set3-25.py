x=[]
y=int(input("value:"))
for i in range(y):
    y=int(input("list:"))
    x.append(y)
    print(sorted(x))
    median=sorted(x)[len(x)//2]
    print(median)
