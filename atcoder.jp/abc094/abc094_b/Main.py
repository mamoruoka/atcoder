n,m,x=map(int,input().split())

A=list(map(int,input().split()))

A.append(x)
A.sort()
idx=A.index(x)

a=A[:idx]
b=A[idx+1:]

print(min(len(a),len(b)))