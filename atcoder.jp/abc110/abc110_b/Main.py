n,m,x,y=map(int,input().split())

X=list(map(int,input().split()))
Y=list(map(int,input().split()))

X.append(x)
X.sort()
Y.append(y)
Y.sort()

if max(X)<min(Y):
    print('No War')
else:
    print('War') 