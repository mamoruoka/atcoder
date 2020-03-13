n,m=map(int,input().split())
X=[]
for i in range(m):
    x=list(map(int,input().split()))
    X.append(x)
P=list(map(int,input().split()))

ans=0

for i in range(2**n):
    B=[]
    b=format(i,'b')
    b=b.zfill(n)
    for j in range(n):
        B.append(int(b[j]))
    flag=True
    for k in range(m):
        cnt=0
        for l in range(X[k][0]):
            cnt+=B[X[k][l+1]-1]
        if cnt%2!=P[k]:
            flag=False
    if flag:
        ans+=1
        
print(ans)