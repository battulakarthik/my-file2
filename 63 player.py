n=int(input())
lst1=[int(x) for x in input().split()]
lst2=[int(x) for x in input().split()]
c=[]
for i in lst1:
    for j in lst2:
        if i==j:
            c.append(i)
for i in range(0,len(c)):
    if i<len(c)-1:k=' '
    else:k=''
    print(c[i],end=k)
