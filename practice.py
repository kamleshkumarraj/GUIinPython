a,b,c,d,e=input("enter number=").split(",")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
k=a
for i in range(k,100000):
    if(i%a==0 and i%b==0 and i%c==0 and i%d==0 and i%e==0 ):
        print(i)
        break
