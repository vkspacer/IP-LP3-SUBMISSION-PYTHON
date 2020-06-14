a=int(input())
b=int(input())
c=min(a,b)
sum=0
for i in range(1,c+1):
    if(a%i==0 and b%i==0):
        sum=sum+1
print(sum)