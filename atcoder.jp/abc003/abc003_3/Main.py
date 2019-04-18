n,k=map(int,input().split())
R=list(map(int,input().split()))

R=sorted(R,reverse=True)
ans=0
for i in range(k):
    ans+=R[i]/(2**(i+1))
print(ans)