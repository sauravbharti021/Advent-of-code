import functools
import math
import collections

from queue import Queue
import sys
import json
import copy

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

d=[[0,1],[0,-1],[1,0],[-1,0]]

g= arr.copy()
for i in range(n):
    g[i]=list(g[i])


x,y=-1,-1
for i in range(n):
    for j in range(m):
        if(arr[i][j]=='S'):
            x=i
            y=j
            break

q= collections.deque()

q.append((x,y))

cnt=0
st= set()
st.add((x,y))

var=64

while(cnt<var):

    size=len(q)
  
    while size>0 and cnt<var:
        (u,v)= q.popleft()
        # print(st)
        st.remove((u,v))
        g[u][v]='.'

        for i in range(4):
            o=u+d[i][0]
            p=v+d[i][1]

            if(o<n and o>=0 and p>=0 and p<m):
                if(g[o][p]!='#' and (o,p) not in st):
                    g[o][p]='O'
                    q.append((o,p))
                    st.add((o,p))
        size-=1
    
    cnt+=1
    

ans=0
if(g[x][y]!='O'):
    g[x][y]='S'


for i in range(n):
    for j in range(m):
        if(g[i][j]=='O' or g[i][j]=='S'):
            ans+=1

print(ans)
