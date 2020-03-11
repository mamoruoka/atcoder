n=int(input())
A=[0]*105
for i in range(1,n+1):
    x=str(i)
    A[int(x[0]+x[len(x)-1])]+=1
ans=0
for i in range(11,100):
    y=str(i)
    if '0' in y:
        continue
    ans+=A[i]*A[int(y[1]+y[0])]
print(ans)