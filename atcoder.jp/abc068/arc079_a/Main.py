n,m=map(int,input().split())
X=[]
for i in range(m):
    a,b=map(int,input().split())
    X.append([a,b])
    
I=[e for i,e in X if i==1]

E=[i for i,e in X if e==n]



if set(I)&set(E)!=set():
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')