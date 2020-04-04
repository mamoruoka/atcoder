n,m=map(int,input().split())
A=list(map(int,input().split()))

cnt=0

s=sum(A)

for i in range(n):
    if A[i]>=s/(4*m):
        cnt+=1
if cnt>=m:
    print('Yes')
else:
    print('No')