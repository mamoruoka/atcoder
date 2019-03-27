n=int(input())
S=[]
X=[]
for i in range(n):
    s=int(input())
    S.append(s)
    if s%10!=0:
        X.append(s)
ans=sum(S)

if ans%10==0:
    if len(X)!=0:
        print(ans-min(X))
    else:
        print(0)
else:
    print(ans)