n=int(input())
c=0
if n>=1 and n<=100000:
    for i in range(0,n):
        if i**2==n:
            c=1
if c==1 or n==1:
    print("yes")
else:print("no")

