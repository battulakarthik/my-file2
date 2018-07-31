nm=[x for x in input()]
count=1
count1=0
k=0
c=''
for i in range(0,len(nm)):
    count=0
    for j in range(i+1,len(nm)):
        if nm[i]==nm[j]:
            count=count+1
            count1=count
        if count1>k:
            k=count
            c=nm[i]
print(c[0])

