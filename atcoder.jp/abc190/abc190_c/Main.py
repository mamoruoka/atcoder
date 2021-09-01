
n,m=map(int, input().split())
X=[]
for i in range(m):
    a, b=map(int, input().split())
    X.append([a,b])
k=int(input())
H = []
for i in range(k):
    c, d=map(int,input().split())
    H.append([c,d])

Ans=0

for i in range(2**k):
    Y = [0]*(n+1)
    b = format(i, 'b').zfill(k)
    for j in range(k):
        if b[j] == '1':
            Y[H[j][0]] = 1
        else:
            Y[H[j][1]] = 1

    ans=0
    for l in range(m):
        if Y[X[l][0]] == 1 and Y[X[l][1]] == 1:
            ans+=1
    Ans = max(Ans, ans)
print(Ans)

