import bisect
n=int(input())
L=list(map(int,input().split()))

L.sort()
cnt=0
for i in range(n-2):
    for j in range(i+1,n-1):
        if L[i]+L[j]<=L[j+1]:
            continue
        if L[i]+L[j]>L[n-1]:
            cnt+=n-j-1
            continue
        index=bisect.bisect_left(L,L[i]+L[j])
        cnt+=index-j-1
print(cnt)