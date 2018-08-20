nm=input()
count=0
coun=0
for i in range(0,len(nm)):
    if nm[i]=="(":
        count+=1
    elif nm[i]==")":
        coun+=1
if count==coun:
    print("yes")
else:print("no")
