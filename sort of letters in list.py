nm=int(input())
lst=[x for x in input().split()]
lst.sort()
for i in range(0,nm):
    for j in range(0,nm):
        if len(lst[j])>len(lst[i]):
            lst[i],lst[j]=lst[j],lst[i]
for i in range(0,nm):
    if i<nm-1:
        k=' '
    else:k=''
    print(lst[i],end=k)
