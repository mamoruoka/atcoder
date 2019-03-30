s=input()

s=s[::-1]

X=['maerd','remaerd','esare','resare']
ans='YES'
i=0
while i<=len(s)-5:
    if s[i:i+5] in X:
        i+=5
    else:
        if s[i:i+6] in X:
            i+=6
        else:
            if s[i:i+7]  in X:
                i+=7
            else:
                ans='NO'
                break

print(ans)