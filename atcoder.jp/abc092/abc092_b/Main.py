n=int(input())
d,x=map(int,input().split())
A=[]
for i in range(n):
    A.append(int(input()))
cnt=0
for j in range(n):
    cnt+=(d-1)//A[j]+1
print(x+cnt)