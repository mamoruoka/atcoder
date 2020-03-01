n=int(input())
X=list(map(int,input().split()))
A=[]
for i in range(min(X),max(X)+1):
    s=0
    for j in range(n):
        s+=(i-X[j])**2
    A.append(s)
print(min(A))