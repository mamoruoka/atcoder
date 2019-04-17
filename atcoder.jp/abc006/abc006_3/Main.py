n,m=map(int,input().split())


if n*2>m:
    print('-1 -1 -1')
elif m>n*4:
    print('-1 -1 -1')
else:
    if n*2<=m and m<n*3:
        print(str(3*n-m)+' '+str(m-2*n)+' '+'0')
    elif n*3<=m and m<=n*4:
        print('0'+' '+str(4*n-m)+' '+str(m-3*n))