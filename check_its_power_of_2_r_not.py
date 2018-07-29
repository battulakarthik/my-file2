nm=int(input())
if nm>=0 and (nm&(nm-1)==0):
    print("yes")
else:
    print("no")
