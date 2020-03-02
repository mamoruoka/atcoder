n=int(input())
a=list(map(int,input().split()))
c=0
d=1
for i in range(n):
    if a[i]==d:
        c+=1
        d+=1
if c==0:
    print(-1)
else:
    print(n-c)