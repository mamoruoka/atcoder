n,m=map(int,input().split())
par=[-1]*n

def find(x):
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
 
def union(x,y):
  x,y=find(x),find(y)
  if x!=y:
    if x>y:
        x,y=y,x
    par[x]+=par[y]
    par[y]=x


A=list(map(int,input().split()))
B=list(map(int,input().split()))
M=[]
for i in range(m):
    c,d=map(int,input().split())
    union(c-1,d-1)

X=[0]*n
Y=[0]*n

for i in range(n):
    if par[i]<0:
        X[i]+=A[i]
        Y[i]+=B[i]
    else:
        X[find(i)]+=A[i]
        Y[find(i)]+=B[i]
if all([x==y for x,y in zip(X,Y)]):
    print('Yes')
else:
    print('No')
