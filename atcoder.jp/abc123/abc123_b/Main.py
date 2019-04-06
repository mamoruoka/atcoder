a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

X=[a,b,c,d,e]
M=[]
for i in X:
   M.append((10-i%10)%10)

ans=0

for i in X:
    ans+=(i+((10-i%10)%10))

print(ans-max(M))