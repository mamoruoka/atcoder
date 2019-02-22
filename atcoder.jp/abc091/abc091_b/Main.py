n=int(input())
S=[]
for i in range(n):
    S.append(input())

m=int(input())
T=[]
for j in range(m):
    T.append(input())

res=0
for i in range(n):
    x=S.count(S[i])
    y=T.count(S[i])
    if x-y>res:
        res=x-y
for j in range(m):
    x=S.count(T[j])
    y=T.count(T[j])
    if x-y>res:
        res=x-y

print(res)