import math
n=int(input())
ans=0
for i in range(1,int(math.sqrt(n*2)+1)):
    if (n*2)%i==0:
        if i%2==0 and ((n*2)//i)%2==1:
            ans += 2
        elif i%2==1 and ((n*2)//i)%2==0:
            ans += 2
print(ans)