n=int(input())
ans=0
for a in range(1,int(n**(1/3))+2):
    x = n//a
    for b in range(a,int(x**0.5)+2):
        if x//b<b or a>b:
            continue
        ans += x//b-b+1
print(ans)
