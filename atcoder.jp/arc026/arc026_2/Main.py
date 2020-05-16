from math import sqrt
n=int(input())
ans=0
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        if i==n//i:
            ans+=i
        else:
            ans+=i+(n//i)
if ans-n>n:
    print('Abundant')
elif ans-n<n:
    print('Deficient')
else:
    print('Perfect')