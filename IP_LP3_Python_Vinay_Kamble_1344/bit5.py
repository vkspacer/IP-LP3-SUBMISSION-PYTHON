a=input()
b=[]
b=list(a)
c=[]
d=""
for i in b:
    if c.count(i)==0:
        c.append(i)
for i in c:
    d=d+i
print(d)