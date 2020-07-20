n,m,k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

a=[0]
b=[0]

for i in range(n):
    a.append(a[i]+A[i])
for i in range(m):
    b.append(b[i]+B[i])

ANS=[0]
idx=m

for i in range(n+1):
    x=k-a[i]
    if x<0:
        break
    while b[idx]>x:
        idx-=1
    ANS.append(i+idx)
print(max(ANS))