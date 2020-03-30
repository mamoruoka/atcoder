a,b=map(int,input().split())
A=str(a-1)
l=len(A)
B=str(b)
L=len(B)

dp_a=[[0,0] for _ in range(l+1)]

dp_a[0][0]=1

for i in range(l):
    for j in range(2):
        x=int(A[i])
        for c in range(10):
            if c==4 or c==9:
                continue
            
            if j==0 and c>x:
                continue
            dp_a[i+1][j or c<x]+=dp_a[i][j]


dp_b=[[0,0] for _ in range(L+1)]

dp_b[0][0]=1

for i in range(L):
    for j in range(2):
        x=int(B[i])
        for c in range(10):
            if c==4 or c==9:
                continue
            
            if j==0 and c>x:
                continue
            dp_b[i+1][j or c<x]+=dp_b[i][j]

print(b-a+1-(dp_b[L][0]+dp_b[L][1]-dp_a[l][0]-dp_a[l][1]))