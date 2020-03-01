A=[]
for _ in range(3):
    A.append(list(map(int,input().split())))

n=int(input())

for _ in range(n):
    x=int(input())
    for i in range(3):
        for j in range(3):
            if x==A[i][j]:
                A[i][j]=0
ans='No'
if A[1][1]==0:
    if A[0][0]==0 and A[2][2]==0:
        ans='Yes'
    if A[0][2]==0 and A[2][0]==0:
        ans='Yes'

for i in range(3):
    if A[i][0]==0 and A[i][1]==0 and A[i][2]==0:
        ans='Yes'
    if A[0][i]==0 and A[1][i]==0 and A[2][i]==0:
        ans='Yes'
print(ans)