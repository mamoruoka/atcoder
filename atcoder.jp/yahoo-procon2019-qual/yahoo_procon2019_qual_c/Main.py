k,a,b=map(int,input().split())
count=0
if b<=a+2:
    count=k+1
else:
    if k<=a:
        count=k+1
    else:
        x=(k-(a+1))//2
        y=k-2*x-(a+1)
        count=(b-a)*x+b+y

print(count)