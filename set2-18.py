a=int(input("value:"))
b=int(input("value:"))
for i in range(a+1,b):
    x=str(i)
    l=len(x)
    y=0
    for j in range(0,l):
        c=x[j]
        d=(int(c))**3
        y+=d
    if y==int(x):
        print(x)
