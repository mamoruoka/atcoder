n,t=map(int,input().split())
X=[]
for i in range(n):
    
    b,c=map(int,input().split())
    X.append([b,c])

X.sort(key=lambda x:x[1])
if X[0][1]>t:
    print('TLE')
else:
    Y=[i for i in X if i[1]<=t]
    Y.sort(key=lambda x:x[0])
    print(Y[0][0])