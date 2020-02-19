n,k,q=map(int,input().split())
A=[k-q]*n
for i in range(q):
    A[int(input())-1]+=1

ans=0

for i in range(n):
    if A[i]>0:
        print('Yes')
    else:
        print('No')