from collections import defaultdict
n=int(input())
ans = 0 
d = defaultdict(int)
d[1]+=1
for i in range(2,n+1):
    # iを素因数分解する
    
    while i%(2*2)==0:
        i=i//(2*2)
    x = 3
    for x in range(3, int(i**0.5)+1, 2):
        while i%(x*x)==0:
            i=i//(x*x)
    d[i]+=1
d = dict(d)
for v in d.values():
    ans += v**2
print(ans)



