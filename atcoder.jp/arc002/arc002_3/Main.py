n=int(input())
K=input()
X=[]
s='ABXY'
for i in range(4):
    for j in range(4):
        X.append(s[i]+s[j])
ans=n
for i in range(len(X)-1):
    for j in range(i+1,len(X)):
        y=K
        while X[i] in y:
            y=y.replace(X[i],'L')
        while X[j] in y:
            y=y.replace(X[j],'R')
        ans=min(ans,len(y))
print(ans)
