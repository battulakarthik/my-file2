n=int(input())
lst=[int(x) for x in input().split()]
c=[]
for i in range(0,n):
    mp=1
    for j in range(0,n):
        if i!=j:
            mp*=lst[j]
    c.append(mp)
for i in range(0,n):
    if i<n-1:k=' '
    else:k=''
    print(c[i],end=k)
