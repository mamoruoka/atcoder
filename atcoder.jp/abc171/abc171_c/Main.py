n=int(input())
x=1
X='abcdefghijklmnopqrstuvwxyz'
for i in range(1,100):
    if x<=n<x+26**i:
        n-=x
        cnt=i
        break
    else:
        x+=26**i
ans=''
for i in range(cnt):
    ans=ans+X[n%26]
    n//=26

print(ans[::-1])