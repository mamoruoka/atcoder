n=int(input())

A=list(map(int,input().split()))
sa=sum(A)
S=[]
for i in range(0,n-1):
    sa-=2*A[i]
    S.append(abs(sa))
print(min(S))