n=int(input())
c=[]
for i in range(1,n+1):
    if n%i==0:
        if i%2!=0:
            c.append(i)
for i in range(0,len(c)):
    if i<len(c)-1:k=' '
    else:k=''
    print(c[i],end=k)
