n=int(input())
A=list(map(int,input().split()))
A.sort()
B=[]
for i in range(n-1):
    B.append(A[i+1]-A[i])

s=0
for i in range(n-1):
    s+=B[i]*(n-1-i)*(i+1)
print(s)