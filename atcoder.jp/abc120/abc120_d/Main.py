n,m=map(int,input().split())
par=[-1]*n
def find(n):
    if par[n]<0:
        return n
    else:
        par[n]=find(par[n])
        return par[n]
def union(x,y,s):
    x,y=find(x),find(y) 
    if x!=y:
        if x>y:
            x,y=y,x
        s-=par[x]*par[y]
        par[x]+=par[y]
        par[y]=x
    return s
        
M=[]
for i in range(m):
    a,b=map(int,input().split())
    M.append([a,b])
ANS=[n*(n-1)//2]
s=n*(n-1)//2
for i in reversed(range(1,m)):
    a,b=M[i][0],M[i][1]
    s=union(a-1,b-1,s)
    ANS.append(s)
for ans in ANS[::-1]:
    print(ans)
            