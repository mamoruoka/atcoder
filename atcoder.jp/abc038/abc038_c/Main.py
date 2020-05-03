n=int(input())
A=list(map(int,input().split()))

right=1
ans=0
for left in range(n):
    if left==right:
        right+=1
    while right<n and (A[right-1]<A[right]):
        right+=1
    ans+=right-left
print(ans)