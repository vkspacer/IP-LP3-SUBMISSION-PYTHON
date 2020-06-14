n=int(input())
j=[]
for i in range(0,n):
    j.append(input())
c=[]
for i in j:
    if c.count(i)==0:
        c.append(i)
for i in c:
    print(j.count(i),end=" ")


    
