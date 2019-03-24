n,m=map(int,input().split())

X=[]

for i in range(n):
    X.append(list(map(int,input().split())))

Y=sorted(X,key=lambda x:x[0])

cnt=0
ans=0
for i in range(n):
    cnt+=Y[i][1]
    if cnt>m:
        ad=m-(cnt-Y[i][1])
        ans+=Y[i][0]*ad
        break
    ans+=Y[i][0]*Y[i][1]

print(ans)