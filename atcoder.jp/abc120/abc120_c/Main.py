s=input()

x=s.count('1')
y=s.count('0')

a=max(x,y)
b=min(x,y)

print(len(s)-(a-b))