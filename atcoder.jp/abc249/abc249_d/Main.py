n=int(input())
A=list(map(int,input().split()))
X=[0 for _ in range(2*10**5+1)]
for a in A:
    X[a]+=1
ans=0
mA=max(A)
for i in range(1, mA+1):
    for j in range(1, (mA//i)+1):
        if X[i]>0 and X[j]>0 and X[i*j]>0:
            ans+=X[i]*X[j]*X[i*j]
print(ans)
