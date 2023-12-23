import functools
import math
import collections

from queue import Queue
import sys

sys.setrecursionlimit((10**7))


path = "input.txt"

s="" 
try:
    with open(path) as file:
        s=(file.read())
except Exception as e:
    print(e)

arr=[]
arr= s.split('\n')

n=len(arr)
m= len(arr[0])

dic= dict()
dic['>'] = "E"
dic['<'] = 'W'
dic['^'] = "N"
dic['v'] = "S"

str= arr[0].index('.')
end= arr[n-1].index('.')

dir=[[0,1, ">"],[0,-1, "<"],[1,0, "v"],[-1,0, "^"]]
lol="><v^"



cnt1=0
vc=set()
for i in range(n):
    for j in range(m):
        if(arr[i][j]=='#'): continue
        num=0
        for k in dir:
            if(0<=k[0]+i<n and 0<=k[1]+j<m and arr[k[0]+i][k[1]+j]!='#'):
                num+=1

        if(num>2):
            vc.add((i,j))


adj={}
vc.add((0, str))
vc.add((n-1, end))

for (pr, pv) in vc:
    adj[(pr,pv)]=[]

    q=collections.deque()
    q.append((pr, pv,0))
    seen=set()

    while(len(q)>0):

        r,v,d= q.popleft()
        if((r,v) in seen):
            continue

        seen.add((r,v))
        if((r,v) in vc and (r!=pr or v!=pv)):
            adj[(pr,pv)].append(((r,v), d))
            continue

        for (hr, hv, nd) in dir:
            if(0<=hr+r<n and 0<=hv+v<m and arr[hr+r][hv+v]!='#'):
                # if(arr[r][v] in lol and arr[r][v]!=nd):
                #     continue
                q.append((hr+r, hv+v, d+1))


mx=0
vis= [[False]*m for _ in range(n)]

def dfs(x,y, d):
    global mx

    if(x==n-1 and y==end):
        mx=max(mx, d)

    vis[x][y]=True
    for (t, dis) in adj[(x,y)]:
        (u,v)=t
        if(not vis[u][v]):
            dfs(u,v, d+dis)

    vis[x][y]=False
        

dfs(0, str, 0)

print(mx)
