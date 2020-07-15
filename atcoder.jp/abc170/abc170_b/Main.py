x,y=map(int,input().split())

if any([i*2+(x-i)*4==y for i in range(x+1)]):
    print('Yes')
else:
    print('No')