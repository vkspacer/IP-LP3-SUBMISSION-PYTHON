def min(b,n,m):
	min=9999
	c=[]
	d=[]
	for i in range(n):
		min=9999
		for j in range(m):
			if(b[i][j]<min):
				min=b[i][j]
			elif(b[i][j]==min):
				d.append(-1)
				return d
		c.append(min)
	for i in range(m):
		min=9999
		for j in range(n):
			if(b[j][i]<min):
				min=b[i][j]
			elif(b[i][j]==min):
				d.append(-1)
				return d
		c.append(min)

	return c
def max(b,n,m):
	max=-9999
	c=[]
	d=[]
	for i in range(n):
		max=-9999
		for j in range(m):
			if(b[i][j]>max):
				max=b[i][j]
			elif(b[i][j]==max):
				d.append(-1)
				return d
		c.append(max)
	for i in range(m):
		max=-9999
		for j in range(n):
			if(b[j][i]>max):
				max=b[i][j]
			elif(b[i][j]==max):
				d.append(-1)
				return d
		c.append(max)
	return c

n=int(input())
m=int(input())
matrix=[]
c=0
sum=0
e=[]
f=[]
for i in range(n):
	arr=list(map(int,input().strip().split()))
	c=c+1
	matrix.append(arr)
	if(c==m):
		break

e=min(matrix,n,m)
f=max(matrix,n,m)
if((e[0]==-1 and len(e)==1) or (f[0]==-1 and len(f)==1)):
	print(-1)
else:
	e=list(set(e))
	f=list(set(f))
	sum=sum+len(e)+len(f)
	print(sum)