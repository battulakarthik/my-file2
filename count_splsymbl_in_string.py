nm=input()
b=sum(c.isalpha() for c in nm)
d=sum(c.isdigit() for c in nm)
e=sum(c.isspace() for c in nm)
spsymbl=len(nm)-b-d-e
print(spsymbl)
