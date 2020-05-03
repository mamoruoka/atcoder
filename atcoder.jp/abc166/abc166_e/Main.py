from _collections import defaultdict
n=int(input())
A=list(map(int,input().split()))

X=[A[i]-(i+1) for i in range(n)]
Y=[-A[i]-(i+1) for i in range(n)]
ans=0

P=defaultdict(int)
Q=defaultdict(int)

for x in X:
    P[x]+=1
for y in Y:
    Q[y]+=1

p=set(P.keys())
q=set(Q.keys())

r=p&q

for key in r:
    ans+=P[key]*Q[key]
print(ans)
