from math import sqrt

x, y = map(int, input().split())
n = int(input())
M = []
for i in range(n):
    px, py = map(int, input().split())
    M.append([px, py])
M.append([M[0][0], M[0][1]])
d = 10 ** 4
for i in range(n):
    A=[x-M[i][0],y-M[i][1]]
    B=[M[i+1][0]-M[i][0],M[i+1][1]-M[i][1]]
    d=min(d,abs(A[0]*B[1]-A[1]*B[0])/sqrt(B[0]**2+B[1]**2))
print(d)