n,y=map(int,input().split())

x=y//10000
ans="-1 -1 -1"
for i in range(x+1):
    for j in range(n-i+1):
        if 10000*i+5000*j+1000*(n-i-j)==y:
            ans=(str(i)+" "+str(j)+" "+str(n-i-j))
            

print(ans)