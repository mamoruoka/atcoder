n=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
s=0
for i in range(n):
    if A[i]>B[i]:
        s+=B[i]
    
    elif A[i]<=B[i] and B[i]<=A[i+1]+A[i]:
        s+=B[i]
        A[i+1]=A[i+1]+A[i]-B[i]
    elif B[i]>A[i+1]+A[i]:
        s+=A[i]+A[i+1]
        A[i+1]=0
print(s)