n,m,c=map(int,input().split())

B=list(map(int,input().split()))

cnt=0
for i in range(n):
    A=list(map(int,input().split()))
    res=c
    for j in range(m):
        res+=A[j]*B[j]
    if res>0:
        cnt+=1
        
print(cnt)