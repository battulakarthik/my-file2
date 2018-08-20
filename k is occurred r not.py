n,m=map(int,input().split())
count=0
while n>0:
    rem=n%10
    if rem==m:
        count+=1
    n=n//10
print(count)
