n=int(input())
A=list(map(int,input().split()))
ans=1
for i in range(n):
    ans*=A[i]
    if ans>10**18:
        ans=-1
        break
if 0 in A:
    ans=0
print(ans)