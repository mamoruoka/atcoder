n,x,y=map(int,input().split())
x-=1
y-=1
D=[[0]*n for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        D[i][j]=min(abs(j-i),abs(x-i)+1+abs(y-j),abs(x-j)+1+abs(y-i))

K=[0]*(n-1)

for i in range(n-1):
    for j in range(i+1,n):
        K[D[i][j]-1]+=1

for k in K:
    print(k)