a=int(input("value:"))
x=a
y=0
while(a>0):
    z=a%10
    y=y*10+z
    a=a//10
if(x==y):
    print ("yes")
else:
    print("no")
