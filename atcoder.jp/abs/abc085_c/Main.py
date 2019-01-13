n,y=map(int,input().split())
Y=y/1000
 
flag=False
 
 
for a in range(0,n+1):
    for b in range(0,n+1):
        if(9*a+4*b==Y-n and a+b<=n):
            flag=True
            print(str(int(a))+" "+str(int(b))+" "+str(int(n-a-b)))
            break
    if flag:
        break
        
if flag == False:
    print("-1 -1 -1")