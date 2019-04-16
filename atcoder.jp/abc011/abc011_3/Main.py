n=int(input())
a=int(input())
b=int(input())
c=int(input())

X=[a,b,c]


ans='YES'

if a==n or b==n or c==n:
    ans='NO'

for i in range(100):
    n-=3
    if n==a or n==b or n==c:
        n+=1
        if n==a or n==b or n==c:
            n+=1
            if n==a or n==b or n==c:
                ans='NO'
                break
if n>0:
    ans='NO'

print(ans)