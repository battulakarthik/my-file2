nm=int(input())
a = [int(x) for x in input().split()]
count=0
for i in range(0,nm):
    j=i+1
    if j+1<nm:
        if a[i]==a[j]:
            count+=1
        if count==1:
            k=a[i]
            print(k)
            break
else:
    print("unique")
