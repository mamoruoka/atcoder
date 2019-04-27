import fractions

n=int(input())
A=list(map(int,input().split()))

X=[A[0]]
Y=[A[-1]]


a=A[0]
for i in range(1,n):
    a=fractions.gcd(A[i],a)
    X.append(a)
b=A[-1]
for i in range(1,n):
    b=fractions.gcd(A[-i-1],b)
    Y.append(b)
    
    
M=[X[-1],Y[-1],X[-2],Y[-2]]
for i in range(1,n-1):
    m=fractions.gcd(X[i-1],Y[-i-2])
    M.append(m)
print(max(M))
    