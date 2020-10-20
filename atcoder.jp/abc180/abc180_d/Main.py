x,y,a,b=map(int,input().split())
ans=0
while x*a<=b+x and x*a<y:
    x*=a
    ans+=1
ans+=(y-1-x)//b

print(ans)