n=int(input())
A=list(map(int,input().split()))

for i in range(n):
    while A[i]%2==0:
        A[i]//=2

print(len(set(A)))