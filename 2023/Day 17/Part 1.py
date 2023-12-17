import functools
import math
import collections

from queue import Queue


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



q= collections.deque()

st= set()
dic= dict()

q.append(((0,0),'W'))

dic[((0,0), 'W')]= (int(arr[0][0])) 

q.append(((0,0), 'S'))
dic[((0,0), 'S')]= (int(arr[0][0])) 

print(st, dic, q)


while(len(q)>0):

    ((x,y), d)= q.popleft()

    # print("now", ((x,y), d))
    if(d=='N' or d=='S'):
        sum1=0
        sum2=0
        for i in range(1,4):
            if((y-i)>=0):
                
                sum1+= int(arr[x][y-i])
                if( ((x,y-i), 'W') not in dic or   (dic[((x, y-i), 'W')]> (dic[((x,y),d)] + sum1 )) ):
  
                    dic[((x, y-i), 'W')]= (dic[((x,y),d)] + sum1)
                    q.append(((x,y-i), 'W'))


            if((y+i)<m):
                sum2+= int(arr[x][y+i])

                if( ((x,y+i), 'E') not in dic or   (dic[((x, y+i), 'E')]> (dic[((x,y),d)] + sum2)) ):

                    dic[((x, y+i), 'E')]= (dic[((x,y),d)] + sum2)
                    q.append(((x,y+i), 'E'))    

    else:
        sum1=0
        sum2=0
        for i in range(1, 11):
            if((x-i)>=0):
                sum1+= int(arr[x-i][y])
                
                if( ((x-i,y), 'N') not in dic or   (dic[((x-i, y), 'N')]> (dic[((x,y),d)] + sum1)) ):

                    dic[((x-i, y), 'N')]= (dic[((x,y),d)] + sum1)
                    q.append(((x-i,y), 'N'))


            if((x+i)<n):

                sum2+= int(arr[x+i][y])

                if( ((x+i,y), 'S') not in dic or   (dic[((x+i, y), 'S')]> (dic[((x,y),d)] + sum2)) ):

                    dic[((x+i, y), 'S')]= (dic[((x,y),d)] + sum2)
                    q.append(((x+i,y), 'S'))   


mi = 1e15

if( ((n-1, m-1), 'N') in dic):
    mi = min(mi, dic[((n-1, m-1), 'N')])
if( ((n-1, m-1), 'S') in dic):
    mi = min(mi, dic[((n-1, m-1), 'S')])
if( ((n-1, m-1), 'E') in dic):
    mi = min(mi, dic[((n-1, m-1), 'E')])
if( ((n-1, m-1), 'W') in dic):
    mi = min(mi, dic[((n-1, m-1), 'W')])

print(mi- int(arr[0][0]))
