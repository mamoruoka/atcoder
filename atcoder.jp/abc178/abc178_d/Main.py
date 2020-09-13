import math
mod=10**9+7
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
s=int(input())
if s<3:
    print(0)
else:
    x=1
    ans=1
    cnt=1
    for i in reversed(range((s-5)%2,s-4,2)):
        if i-cnt<0:
            break
        ans+=combinations_count(i,cnt)
        cnt+=1
    print(ans%mod)