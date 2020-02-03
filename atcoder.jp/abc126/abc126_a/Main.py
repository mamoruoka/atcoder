n,k=map(int,input().split())
s=input()
x=s[k-1].lower()
s=s[:k-1]+x+s[k:]
print(s)