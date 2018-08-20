n,m=map(int,input().split())
k,b=map(int,input().split())
h,j=map(int,input().split())
if n==k==h or m==b==j or (n==m and k==b and h==j):
    print("yes")
else:print("no")
