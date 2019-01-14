s=input()

s=s[::-1]



a="maerd"
b="remaerd"
c="esare"
d="resare"


while(len(s)>=5):
    if(s[:5]==a):
        s=s[5:]
        continue
    if(s[:7]==b):
        s=s[7:]
        continue
    if(s[:5]==c):
        s=s[5:]
        continue
    if(s[:6]==d):
        s=s[6:]
        continue
    else:
        break
    
if(len(s)==0):
    print("YES")
else:
    print("NO")