n,x=map(int,input().split())

A=list(map(int,input().split()))

B=[a for a in A]

if B[0]>x:
    B[0]=x

for i in range(n-1):
    if B[i]+B[i+1]>x:
        B[i+1]=x-B[i]

ans=0
for a,b in zip(A,B):
    ans+=(a-b)

print(ans)