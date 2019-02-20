a,b,c=map(int,input().split())

X=[a,b,c]
X.sort()
x=X[2]
y=X[1]
z=X[0]


sabun1=x-y
sabun2=x-z

if sabun1%2==0 and sabun2%2==0:
    res=(sabun1+sabun2)/2
elif sabun1%2==1 and sabun2%2==1:
    res=(sabun1//2+sabun2//2)+1
elif sabun1%2==0 and sabun2%2==1:
    res=(sabun1/2)+(sabun2//2)+2
else:
    res=(sabun1//2)+(sabun2/2)+2

print(int(res))