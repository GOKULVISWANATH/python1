a=int(input("value:"))
b=int(input("value:"))
if a==1:
    a=a+1
for x in range(a,b+1):
    n=0
    for y in range(2,int(x/2)+1):
        if x%y==0:
            n=1 
            break
    if n==1:
        continue
    print(x)

