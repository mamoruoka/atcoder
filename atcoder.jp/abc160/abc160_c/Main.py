k,n=map(int,input().split())
A=list(map(int,input().split()))
X=[]
for i in range(n-1):
    X.append(A[i+1]-A[i])
X.append(A[0]+k-A[n-1])
print(k-max(X))