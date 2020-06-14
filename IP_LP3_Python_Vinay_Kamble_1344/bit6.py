n=str(input())
b=[]
a=""
b=list(n.split(" "))
for i in b:
    if i=='not':
        c=b.index(i)
        for i in b:
            if i=='poor' or i=='poor!':
                d=b.index(i)
                if d>c:
                    b[c]='good'
                    for j in range(0,c+1):
                        a=a+b[j]
                        a=a+" "
                    print(a)

