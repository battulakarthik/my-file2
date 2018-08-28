n=int(input())
lst=[int(x) for x in input().split()]
for i in range(0,n):
    if i<n-2:k=' '
    else:k=''
    if i<n-1:
        print(max(lst[i],lst[i+1]),end=k)

