n,k=map(int,input().split())
A=[int(input()) for i in range(n)]

X=[]
cnt=1
for i in range(n-1):
    if A[i]>=A[i+1]:
        X.append(cnt)
        cnt=1
    else:
        cnt+=1
X.append(cnt)
ans=0
for x in X:
    if x-k>=0:
        ans+=(x-k)+1

print(ans)