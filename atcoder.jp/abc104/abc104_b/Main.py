s=input()
count=0
if s[0]=='A':
    for i in range(2,len(s)-1):
        if s[i]=='C':
            count+=1
            index=i

    
    if count==1:
        x=s[1:index]+s[index+1:]
        if x.islower():
            print('AC')
        else:
            print('WA')
    else:
        print('WA')
            
else:
    print('WA')