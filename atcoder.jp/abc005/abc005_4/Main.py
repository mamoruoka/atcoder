n=int(input())
T=[list(map(int,input().split())) for _ in range(n)]

q=int(input())

S=[[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        S[i+1][j+1]=S[i][j+1]+S[i+1][j]-S[i][j]+T[i][j]
val=[0]*(n**2+1)
for a in range(n):
    for b in range(a+1,n+1):
        for c in range(n):
            for d in range(c+1,n+1):
                area=(b-a)*(d-c)
                s=S[b][d]-S[a][d]-S[b][c]+S[a][c]
                val[area]=max(val[area],s)

for i in range(n**2):
    val[i+1]=max(val[i+1],val[i])

for i in range(q):
    print(val[int(input())])