n=int(input())
ans=0
for i in range(n-1,0,-1):
    # これまでに取り出されていない玉を取り出す期待値はn/i
    # これを全ての玉が取り出された状態になるまで行う
    ans+=n/i
    
    
print(ans)