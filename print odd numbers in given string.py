nm=[int(x) for x in input()]
lst=[]
for i in range(0,len(nm)):
    if nm[i]%2!=0:
        lst.append(nm[i])
for i in range(0,len(lst)):
    if i<len(lst)-1:
        k=" "
    else:k=''
    print(lst[i],end=k)

