s=input()
cnt_1=0
cnt_2=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        cnt_1+=1
for i in range(len(s)-1,0,-1):
    if s[i]!=s[i-1]:
        cnt_2+=1

print(min(cnt_1,cnt_2))