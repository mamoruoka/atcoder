n=int(input())
A=list(map(str,input().split()))
   
if len(set(A))==3:
    print('Three')
else:
    print('Four')