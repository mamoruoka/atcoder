s=input()

for i in range(len(s)-2,0,-2):
    s=s[:i]
    if s[:i//2]==s[i//2:]:
        print(len(s))
        break