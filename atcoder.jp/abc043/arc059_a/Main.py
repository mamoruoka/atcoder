n=int(input())
A=list(map(int,input().split()))
A.sort()
ans=10**9

for i in range(A[0],A[n-1]+1):
    res=0
    for j in range(n):
        res+=(i-A[j])**2
    ans=min(ans,res)

print(ans)
        