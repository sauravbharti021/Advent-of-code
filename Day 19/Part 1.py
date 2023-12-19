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

inp= collections.defaultdict(list)

after=-1
for i in range(n):
    if(arr[i]==""):
        after=i
        break
    else: 
        lol= arr[i].split('{')
        yo= lol[1].split('}')
        heh= yo[0].split(',')
        for j in heh:
            inp[lol[0]].append(j)


dic=dict()

def check(direction, x, m, a, s, flag):
  
    for i in range(len(inp[direction])):
        dest=""
        if(':' not in inp[direction][i]):
            dest= inp[direction][i]
            if(dest=='A'):
                flag=True
                return flag
            elif(dest=='R'):
                flag=False
                return flag
            else:
                flag= check(dest, x, m, a, s,flag)
                return flag
            
        temp= inp[direction][i].split(':')
        dest=temp[1]

        cond= temp[0][1]
        num= temp[0][2::]

        variable= None
        if(temp[0][0]=='x'): variable=x
        elif(temp[0][0]=='m'): variable=m
        elif(temp[0][0]=='a'): variable=a
        else: variable=s
        if(cond=='>'):
            if(variable>int(num)):
                if(dest=='A'):
                    flag=True
                    return flag
                elif(dest=='R'):
                        flag=False
                        return flag
                else:
                    flag=check(dest, x, m, a, s,flag)
                    return flag
        else:
            if(variable<int(num)):
                if(dest=='A'):
                    flag=True
                    return flag
                elif(dest=='R'):
                        flag=False
                        return flag
                else:
                    flag=check(dest, x, m, a, s,flag)
                    return flag

    return flag


sum_v=[]

for i in range(after+1, n):
    heh= arr[i][1:-1]
    now=heh.split(',')
    vals=[]
    for j in now:
        fin= j.split('=')
        vals.append(int(fin[1]))

    x,m,a,s=vals[0],vals[1],vals[2],vals[3]
    if(check("in", x,m,a,s, False)):
        sum_v.append(sum(vals))

print(sum(sum_v))
