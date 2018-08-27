n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
c=[]
for i in range(0,len(lst)):
    if lst[i]<m:
        c.append(lst[i])
c.sort()
for i in range(0,len(c)):
    if i<len(c)-1:k=' '
    else:k=''
    print(c[i],end=k)
