X=[]
n=int(input())
for i in range(n):
    t,a=map(int,input().split())
    X.append([t,a])

T=X[0][0]
A=X[0][1]

for i in range(1,n):
    N=max(-(-T//X[i][0]),-(-A//X[i][1]))
    T=X[i][0]*N
    A=X[i][1]*N
print(T+A)
        