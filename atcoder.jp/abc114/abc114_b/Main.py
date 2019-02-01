s=input()
X=[]
for i in range(len(s)-2):
    num=s[i]+s[i+1]+s[i+2]
    X.append(abs(int(num)-753))

print(min(X))