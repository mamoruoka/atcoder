n,k=map(int,input().split())
A=list(map(int,input().split()))
cnt=0
s=1
M=[0]
B=[False]*(n+1)
while cnt<n:
    s=A[s-1]
    if not B[s-1]:
        B[s-1]=True
    else:
        break
    M.append(s-1)
    cnt+=1
x=M.index(s-1)
y=len(M)-x

if k<=x:
    print(M[k]+1)
else:
    N=M[x:]
    print(N[(k-x)%y]+1)