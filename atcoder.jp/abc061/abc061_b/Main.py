n,m=map(int,input().split())
X=[]
for i in range(m):
    a,b=map(int,input().split())
    X.append(a)
    X.append(b)

for i in range(1,n+1):
    print(X.count(i))   