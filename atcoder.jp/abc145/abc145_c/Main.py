import math

n=int(input())
M=[]
for i in range(n):
    x,y=map(int,input().split())
    M.append([x,y])

D=[]
for i in range(n-1):
    for j in range(i+1,n):
        D.append(math.sqrt((M[i][0]-M[j][0])**2+(M[i][1]-M[j][1])**2))

print(sum(D)*2/n)