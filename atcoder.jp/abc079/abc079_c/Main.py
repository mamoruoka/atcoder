s=input()

a=s[0]
b=s[1]
c=s[2]
d=s[3]

op=['+','-']

for i in op:
    for j in op:
        for k in op:
            if eval(str(a)+i+str(b)+j+str(c)+k+str(d))==7:
                ans=str(a)+i+str(b)+j+str(c)+k+str(d)+'=7'

print(ans)