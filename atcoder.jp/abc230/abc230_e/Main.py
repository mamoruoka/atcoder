n=int(input())
ans=0
cnt=n
for i in range(1,int(n**0.5)+1):
    ans+=n//i
    if i==n//i:
        continue
    # 答えに足すものがiになるやつは次の奴との差だけある
    ans+=i*(n//i-n//(i+1))
print(ans)
    

        