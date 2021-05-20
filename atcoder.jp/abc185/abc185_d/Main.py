n,m=map(int,input().split())
A=list(map(int,input().split()))
A.append(0)
A.append(n+1)
A.sort()
B=[]
for i in range(len(A)-1):
    if A[i+1] - A[i] != 1 and A[i+1] - A[i] !=0:
        B.append(A[i+1] - A[i] - 1)
ans=0
if B:
    x=min(B)
for b in B:
    ans+=-1*(-b//x)
print(ans)