k=int(input())
c=7
a=-1
for i in range(1,10**6):
    c%=k
    if c%k==0:
        a=i
        break
    else:
        c*=10
        c+=7
print(a)