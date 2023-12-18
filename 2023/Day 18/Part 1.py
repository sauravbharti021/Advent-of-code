import functools
import math
import collections

from queue import Queue
import sys

sys.setrecursionlimit(10**7)


path = "input.txt"

s="" 
try:
    with open(path) as file:
        s=(file.read())
except Exception as e:
    print(e)


arr= s.split('\n')

n=len(arr)
m=len(arr[0])

dic= dict()
dic['D'] = (1,0)
dic['U']= (-1,0)
dic['R'] = (0, 1)
dic['L'] = (0, -1)



def shoelace():
    total_area=0
    for i in range(len(points)):
        up= points[i]
        down= points[(i+1)%(len(points))]

        total_area += (up[0]*down[1])-(up[1]*down[0])

    return abs(total_area)/2

points=[]

tot=0
for i in arr:
    temp= i.split(' ')

    (u,v) = dic[temp[0]]
    for j in range(int(temp[1])):
        x+=u
        y+=v
        points.append((x,y))
        tot+=1

print( round(shoelace() + tot/2 + 1))

