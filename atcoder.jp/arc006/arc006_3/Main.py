import bisect
n=int(input())
X=[int(input()) for _ in range(n)]

A=[X[0]]

for i in range(1,n):
    if X[i]>A[-1]:
        A.append(X[i])
    elif X[i]<A[-1]:
        j=bisect.bisect_left(A,X[i])
        A[j]=X[i]
print(len(A))