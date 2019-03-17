n=int(input())
k=int(input())
res=1
for i in range(n):
    if res>k:
        res+=k
        break
    res*=2


res+=k*(n-i-1)

print(res)