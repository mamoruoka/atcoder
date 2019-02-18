n,x=map(int,input().split())
A=[]
for i in range(n):
    A.append(int(input()))

s=int((x-sum(A))/min(A))

print(s+n)