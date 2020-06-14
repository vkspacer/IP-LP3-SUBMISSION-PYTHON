def func(n,x):
    s=0
    while(n-x>0):
        s=s+n-x
        x=x+2
    return s
n=int(input())
x=0
sum=func(n,x)
print(sum)
