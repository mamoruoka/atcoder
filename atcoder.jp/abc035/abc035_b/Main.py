s=input()
t=int(input())

abs_x=0
abs_y=0

hatena_count=0

for i in range(len(s)):
    if(s[i]=="U"):
        abs_y+=1
    elif(s[i]=="D"):
        abs_y-=1
    elif(s[i]=="R"):
        abs_x+=1
    elif(s[i]=="L"):
        abs_x-=1
    else:
        hatena_count+=1

abs_x=abs(abs_x)
abs_y=abs(abs_y)

if(t==1):
    print(abs_x+abs_y+hatena_count)
else:
    if(abs_x+abs_y-hatena_count>=0):
        print(abs_x+abs_y-hatena_count)
    else:
        print((hatena_count-abs_x-abs_y)%2)