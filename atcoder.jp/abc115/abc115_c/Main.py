n,k=map(int,input().split())

x=[]
for i in range(n):
    x.append(int(input()))

x.sort()

y=[]

for j in range(n-k+1):
  p=x[j+k-1]-x[j]
  y.append(p)

y.sort()

print(y[0])