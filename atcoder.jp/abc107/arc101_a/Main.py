n,k=map(int,input().split())

X=list(map(int,input().split()))
V=[]
for i in range(n-k+1):
    Y=X[i+k-1]-X[i]   
    V.append(Y+min(abs(X[i]),abs(X[i+k-1])))

print(min(V))