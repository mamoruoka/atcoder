n=int(input())
X=[0]*(10**6+2)
B=0
for i in range(n):
    a,b=map(int,input().split())
    X[a]+=1
    X[b+1]-=1
    B=max(B,b)
res=0
ans=0
for i in range(B+1):
    res+=X[i]
    ans=max(ans,res)

print(ans)