n=int(input())
cnt_10=0
if n%2==1:
    print(0)
else:
    for j in range(1,100):
        cnt_10+=n//(2*5**j)  
    print(cnt_10)