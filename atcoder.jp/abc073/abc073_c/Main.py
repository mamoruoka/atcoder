import collections
n=int(input())
A=[]
for i in range(n):
    A.append(int(input()))

x=collections.Counter(A)
cnt=0
for v in x.values():
    if v%2==1:
        cnt+=1

print(cnt)
    