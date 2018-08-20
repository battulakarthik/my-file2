n,mm=map(int,input().split())
if n>mm:
    sm=n
else:sm=mm
for i in range(1,sm+1):
    if(n%i==0) and (mm%i==0):
        g=i
print(g)
