a,b,k=map(int,input().split())
X=[]
for i in range(a,a+k):
    if i>b:
        break
    X.append(i)
    
    
for j in range(b-k+1,b+1):
    if j<a:
        break
    X.append(j)
    
X=set(X)
X=list(X)
X.sort()

for i in range(len(X)):
    print(X[i])