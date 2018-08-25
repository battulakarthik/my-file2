n,m=input().split()
c=0
for i in n:
    if i in m:
        c=1
if c==1:print("yes")
else:print("no")
