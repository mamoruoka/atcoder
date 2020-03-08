n=int(input())

A=[0]+list(map(int,input().split()))

for i in reversed(range(1,n+1)):
    if sum(A[::i])%2!=A[i]:
        if A[i]==0:
            A[i]=1
        else:
            A[i]=0
        
print(sum(A))
if sum(A)!=0:
    for i,a in enumerate(A):
        if a==1:
            print(i)