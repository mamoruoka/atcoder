s=input()
cnt=0

if s!='1': 
    for i in range(0,len(s),2):
        if s[i]=='0':
            cnt+=1
    for j in range(1,len(s),2):
        if s[j]=='1':
            cnt+=1
else:
    cnt=0

print(min(cnt,len(s)-cnt))