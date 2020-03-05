n=int(input())

A=list(map(int,input().split()))

s=sum(A)
for i in range(2,n,2):
    s-=2*A[i-1]
    ans=str(s)+' '
for j in range(n-1):
    s=2*A[j]-s
    ans+=str(s)+' '

print(ans)