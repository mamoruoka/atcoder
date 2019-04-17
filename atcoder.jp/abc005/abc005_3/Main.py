t=int(input())
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split())) 
ans='yes'
if n<m:       
    ans='no'
else:
    cnt=0
    for i in range(n):
        if A[i]<=B[cnt] and B[cnt]<=A[i]+t:
            cnt+=1
            if cnt==m:
                break
    if cnt!=m:
        ans='no'

print(ans)
