import numpy as np
n=int(input())
x,y=map(int,input().split())
X,Y=map(int,input().split())

cx=(x+X)/2
cy=(y+Y)/2

vec_x=x-cx
vec_y=y-cy

vec=np.array([vec_x, vec_y])
Rot=np.matrix([[np.cos(2*np.pi/n), np.sin(2*np.pi/n)],
               [-np.sin(2*np.pi/n), np.cos(2*np.pi/n)]])
res_vec=np.dot(vec,Rot)
print(cx+res_vec[0,0], cy+res_vec[0,1])           