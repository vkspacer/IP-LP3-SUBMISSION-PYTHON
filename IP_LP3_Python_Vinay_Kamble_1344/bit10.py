def sort(n,b):
    for i in range(0,n-1):
        minn=b[i]
        pos=i
        for j in range(i+1,n):
            if(b[j]<minn):
                minn=b[j]
                pos=j
        b[pos]=b[i]
        b[i]=minn
    print(b)
n=int(input())
b=[]
b=list(map(int,input().split()))
sort(n,b)