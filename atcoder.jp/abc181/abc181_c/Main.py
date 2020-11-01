n=int(input())
M=[]
ans='No'
for i in range(n):
    x,y=map(int,input().split())
    M.append([x,y])
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a=M[i][0]
            b=M[i][1]
            c=M[j][0]
            d=M[j][1]
            e=M[k][0]
            f=M[k][1]
            if (b-d)*(e-c)==(a-c)*(f-d):
                ans='Yes'
print(ans)