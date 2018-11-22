n=int(input())
lst=[int(x) for x in input().split()]
res=[]

for i in range(0,n-1):
    if lst[i]>lst[i+1]:
        res.append(lst[i+1])
    else:res.append(-1)
    if i==n-2:
        res.append(-1)
for i in range(0,n):
    if i<n-1:
        k=' '
    else:k=''
    print(res[i],end=k)

