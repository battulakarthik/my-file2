n=input()
n=list(n)
c=len(n)
if n[::-1]==n:
    for i in range(0,c-1):
        print(n[i],end='')
else:
    for i in range(0,c):
        print(n[i],end='')
