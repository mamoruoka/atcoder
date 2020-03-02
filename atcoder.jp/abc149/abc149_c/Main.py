x=int(input())
ans=100003  
for i in range(x,10**5+1):
    if all(i%j!=0 for j in range(2,x)):
        ans=i
        break
print(ans)