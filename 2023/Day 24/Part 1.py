import functools
import math
import collections

from queue import Queue
import sys

sys.setrecursionlimit((10**7))


path = "C:\\Users\\saura\\Desktop\\PROJECT\\scaler\\input.txt"

s="" 
try:
    with open(path) as file:
        s=(file.read())
except Exception as e:
    print(e)

arr=[]
arr= s.split('\n')

n=len(arr)

v=[]
for i in range(n):
    arr[i]= arr[i].replace('@', ',')

    temp= arr[i].split(',')
    now=[]
    for j in temp:
        now.append(int(j))

    v.append(now)

ans=0
for ind, i in enumerate(v):
    for j in v[:ind]:
        # print(i,j)
        x1= i[0]
        y1=i[1]
        z1=i[2]
        x2= i[0]+ i[3]
        y2= i[1]+i[4]

        x3=j[0]
        y3=j[1]
        z3=j[2]
        x4=j[0]+j[3]
        y4=j[1]+j[4]

        deno=   ((x1- x2)*(y3-y4) - (y1-y2)*(x3-x4))

        if(deno!=0):
            px =  ((x1*y2 - y1*x2)* (x3-x4) - (x1-x2)*(x3*y4 - y3*x4))/ deno

            py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)) /deno     

            flag1= (px<x1) == (x2<x1)
            flag2= (px<x3) == (x4<x3)

            if(200000000000000<=px<=400000000000000 and 200000000000000<=py<=400000000000000 and flag1 and flag2):
                ans+=1


print(ans)

            
