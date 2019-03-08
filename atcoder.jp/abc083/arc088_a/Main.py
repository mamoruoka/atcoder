x,y=map(int,input().split())
a=x
cnt=0
while a<=y:
    a=a*2
    cnt+=1

print(cnt)