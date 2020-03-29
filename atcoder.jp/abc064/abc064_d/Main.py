n=int(input())
s=input()
z=s
while '()' in s:
    s=s.replace('()','')
print('('*s.count(')')+z+')'*s.count('('))