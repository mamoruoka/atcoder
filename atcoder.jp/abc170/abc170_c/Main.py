x,n=map(int,input().split())
P=list(map(int,input().split()))
Q=[-1,0]
for i in range(1,102):
    if i not in P:
        Q.append(i)

ans=10**9
A=[]
for i,q in enumerate(Q):
    A.append([i,abs(q-x)])
A.sort(key=lambda x:(x[1],x[0]))
print(Q[A[0][0]])