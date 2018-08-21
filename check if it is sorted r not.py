n=int(input())
lst=[int(x) for x in input().split()]
c=(sorted(lst))
count=0
for i in range(0,n):
    if lst[i]==c[i]:
        count+=1
if count==n:
    print("yes")
else:print("no")
