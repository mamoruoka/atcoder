a,b=map(int,input().split())

if a%2==0:
    fa=(a//2)%2
else:
    fa=(((a-1)//2)%2)^(a-1)

if b%2==0:
    fb=((b//2)%2)^b
else:
    fb=((b+1)//2)%2
    
print(fb^fa)