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

arr=[]
arr= s.split('\n')

for i in range(len(arr)):
    arr[i]=list(arr[i])

n=len(arr)
m=len(arr[0])

temp= arr.copy()

ans=[]

for i in range(m):
    cnt=0
    lol=[]
    for j in range(n-1, -1, -1):

        if(temp[j][i]=='O'):
            cnt+=1
        elif(temp[j][i]=='#' and cnt>0):
            for k in range(j, n):
                if((temp[k][i]=='O' or temp[k][i]=='.') and cnt>0):
                    cnt-=1
                    ans.append((n-k))
                    lol.append((n-k))
                
            cnt=0


    if(cnt>0):
        for j in range(n):
            if((temp[j][i]=='O' or temp[j][i]=='.') and cnt>0):
                cnt-=1
                ans.append((n-j))
                lol.append((n-j))
            elif(temp[j][i]=='#'):
                break
            

for i in temp:
    print(i)

print(sum(ans))
