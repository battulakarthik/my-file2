n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
for i in range(0,n):
    c=1
    for j in range(i+1,n):
        if lst[i]==lst[j]:
            c+=1
            if c==m:
                tm=lst[i]
print(tm)
