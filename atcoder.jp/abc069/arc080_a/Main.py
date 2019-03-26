n=int(input())

A=list(map(int,input().split()))

cnt_4=0

cnt_2=0

for i in A:
    if i%4==0:
        cnt_4+=1
    elif i%2==0:
        cnt_2+=1


if cnt_4>=(n//2):
    print('Yes')
else:
    if 2*cnt_4+cnt_2>=n:
        print('Yes')
    else:
        print('No')