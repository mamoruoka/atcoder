import itertools
s=input()
C=['+','']
X=list(itertools.product(C,repeat=len(s)-1))
ans=0
for i in range(len(X)):
    res=''
    for j in range(len(s)-1):
        res+=s[j]+X[i][j]
    res+=s[len(s)-1]
    ans+=eval(res)

print(ans)