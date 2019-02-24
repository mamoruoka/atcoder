a,b=map(int,input().split())

x=int(str(a)+str(b))
ans='No'
for i in range(1,400):
    if i*i==x:
        ans='Yes'
print(ans)
