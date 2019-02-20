n=int(input())

res=n
for i in range(n+1):
    count=0
    j=n-i
    while i>0:
        count+=i%6
        i//=6
    while j>0:
        count+=j%9
        j//=9
    if res>count:
        res=count

print(int(res))