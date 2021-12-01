s=input()
k=int(input())
X=[0]*(len(s)+1)
cnt=0
# 累積和は最初が0である必要があるためこのような方法になる
for i in range(len(s)):
    if s[i]==".":
        X[i+1]=X[i]+1
    else:
        X[i+1]=X[i]
ans=0
# ↑のような手法を取ったため
# [l,r)における.の数はX[r]-X[l]で導ける(基本的に半開区間で考える)
r=0
for l in range(len(s)):
    # 条件を満たさないところまで右端を進める
    while r<=len(s)-1 and X[r+1]-X[l]<=k:
        r+=1
    # 現在のrは満たしていないつまりl~r-1までが条件を満たしており、その長さはr-lである
    ans = max(ans, r-l)
print(ans)

