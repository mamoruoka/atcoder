s=input()
a=int(s[:2])
b=int(s[2:])

if (1<=a<=12 and 1<=b<=12):
    print('AMBIGUOUS')
elif (1<=a<=12 and (b>12 or b==0)):
    print('MMYY')
elif ((a>12 or a==0) and 1<=b<=12):
    print('YYMM')
else:
    print('NA')