h,w,m=map(int,input().split())
H=[0]*(3*10**5+1)
W=[0]*(3*10**5+1)
M=[]
for i in range(m):
    h,w=map(int,input().split())
    M.append([h,w])
    H[h]+=1
    W[w]+=1

p=max(H)
q=max(W)

X=set([i for i in range(3*10**5+1) if H[i]==p])
Y=set([i for i in range(3*10**5+1) if W[i]==q])

cnt=0
for i in range(m):
    if M[i][0] in X and M[i][1] in Y:
        cnt+=1

if cnt==len(X)*len(Y):
    print(p+q-1)
else:
    print(p+q)
