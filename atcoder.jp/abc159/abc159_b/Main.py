s=input()
n=len(s)
 
x=s[:(n-1)//2]

y=s[(n+1)//2:]

if s==s[::-1] and x==x[::-1] and y==y[::-1]:
    print('Yes')
else:
    print('No')