n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
c=0
for i in range(n-1,-1,-1):
    lst.pop(i)
    c+=1
    if c==m:
        break
for i in range(0,len(lst)):
    if i<len(lst)-1:k=' '
    else:k=''
    print(lst[i],end=k)
