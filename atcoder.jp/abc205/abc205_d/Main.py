import bisect
n,q=map(int,input().split())
A=list(map(int,input().split()))
K=[]
for _ in range(q):
    K.append(int(input()))

C=[0]*n
for i in range(n):
    C[i]=A[i]-1-i

for k in K:
    if k > C[-1]:
        print((k-C[-1])+A[-1])
    else:
        idx=bisect.bisect_left(C,k)
        print(A[idx]-(C[idx]-k)-1)
