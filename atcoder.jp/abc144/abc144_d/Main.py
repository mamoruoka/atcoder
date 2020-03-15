import math
a,b,x=map(int,input().split())

if x/(a**2)>=b:
    print(0)
elif x/(a**2)>=b*0.5:
    print(90-math.degrees(math.atan((a*0.5)/(b-x/a**2))))
else:
    print(math.degrees(math.atan(b/(2*x/(a*b)))))