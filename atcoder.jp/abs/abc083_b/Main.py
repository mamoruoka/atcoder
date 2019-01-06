n,a,b=map(int,input().split())



sum=0

for i in range(1,n+1):
    o=int(i/10000)
    p=int((i-10000*o)/1000)
    q=int((i-10000*o-1000*p)/100)
    r=int((i-10000*o-1000*p-100*q)/10)
    s=i%10
    
    sum_i=o+p+q+r+s
    
    if(sum_i>=a and sum_i<=b):
        sum+=i

print(sum)