n,m=map(int,input().split())
X=[]
for i in range(m):
    a,b=map(int,input().split())
    X.append([a,b])
X.sort(key=lambda x:x[1])
x=0
ans=0
for i in range(m):
    if X[i][0]<=x:
        continue
    else:
        x=X[i][1]-1
        ans+=1
print(ans)