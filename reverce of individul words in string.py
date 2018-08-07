nm=[x for x in input().split()]
c=[]
for i in range(0,len(nm)):
    f=''
    ch=nm[i]
    for j in range(0,len(ch)):
        f=ch[j]+f
    if i<len(nm)-1:
        k=' '
    else:k=''
    print(f,end=k)
