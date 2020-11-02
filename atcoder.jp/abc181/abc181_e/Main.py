import bisect
import itertools
n,m=map(int,input().split())
H=list(map(int,input().split()))
W=list(map(int,input().split()))

H.sort()

a=[0]+[H[i+1]-H[i] for i in range(0,n-1,2)]
A=list(itertools.accumulate(a))
B=[H[i+1]-H[i] for i in range(1,n,2)]+[0]
for i in range(len(B)-1,0,-1):
    B[i-1]+=B[i]

ans=10**12
for i in range(m):
    x=bisect.bisect_left(H,W[i])
    if x%2==1:
        x-=1
    s = A[x//2]+B[x//2]+abs(H[x]-W[i])
    ans=min(ans,s)

print(ans)
