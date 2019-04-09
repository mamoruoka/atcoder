a,b,c=map(int,input().split())
ans='NO'
for i in range(10**5):
    if (c+b*i)%a==0:
        ans='YES'
        break
print(ans)