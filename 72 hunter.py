str=[x for x in input().split()]
p=0
for i in str:
    if p<len(str)-1:
        k=' '
    else:k=''
    if p%2==0:
        print(i[::-1],end=k)
    else:print(i,end=k)
    p+=1
