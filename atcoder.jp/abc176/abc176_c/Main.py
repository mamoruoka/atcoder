n=int(input())
A=list(map(int,input().split()))

x=A[0]
cnt=0
for i in range(n):
    if A[i]<x:
        cnt+=x-A[i]
    else:
        x=A[i]
print(cnt)