n,k=map(int,input().split())
A=list(map(int,input().split()))

ans=0
s=0

r=0
for l in range(n):
    while s<k:
        if r==n:
            break
        else:
            s+=A[r]
            r+=1
    if s<k:
        break
    ans+=n-r+1
    s-=A[l]
print(ans)