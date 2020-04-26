from collections import defaultdict
s=input()
n=len(s)
N=defaultdict(int)
x=0
for i in reversed(range(n)):
    x+=int(s[i])*pow(10,(n-i-1),2019)
    x%=2019
    N[x]+=1
ans=N[0]
for j in N.values():
    ans+=j*(j-1)//2
print(ans)