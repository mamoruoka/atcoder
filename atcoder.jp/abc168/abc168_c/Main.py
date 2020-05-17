from math import sin,cos,sqrt,pi
a,b,h,m=map(int,input().split())

ta=30*h+m/2
tb=6*m

xa=a*cos(ta*pi/180)
ya=a*sin(ta*pi/180)

xb=b*cos(tb*pi/180)
yb=b*sin(tb*pi/180)

print(sqrt((xa-xb)**2+(ya-yb)**2))