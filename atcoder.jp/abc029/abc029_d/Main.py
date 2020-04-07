n=int(input())
l=len(str(n))
ans=0
for i in range(l):
    ans+=(n//(10**(i+1)))*(10**i)
    if n%(10**(i+1))>=10**i:
        ans+=min(n%(10**(i+1))-10**i+1,10**i)
print(ans)