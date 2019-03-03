n=int(input())

x=str(n)
y=0
for i in range(len(x)):
    y+=int(x[i])

if n%y==0:
    print('Yes')
else:
    print('No')