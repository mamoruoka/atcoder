n=int(input())
A=[]
s=0
for i in range(n):
    a,b=map(int,input().split())
    s-=a
    A.append(2*a+b)

A.sort(reverse=True)

cnt=0

for i in range(n):
    s+=A[i]
    cnt+=1
    if s>0:
        break
print(cnt)