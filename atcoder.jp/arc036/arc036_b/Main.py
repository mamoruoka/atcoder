n=int(input())
H=[]
for i in range(n):
    H.append(int(input()))
if n==1:
    print(1)
elif n==2:
    print(2)
else:     
    ans=0
    s=1
    for i in range(1,n):
        s+=1
        if i==n-1:
            ans=max(ans,s)
            break
        if H[i]<H[i-1] and H[i]<H[i+1]:
            ans=max(ans,s)
            s=1
    print(ans)