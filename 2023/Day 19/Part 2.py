import functools
import math
import collections

from queue import Queue
import sys
import json

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
total=0

def check(direction, mn,mx):
    if(direction=='A'):
        cur=1
        for i in mn.keys():
            cur*= max((mx[i]-mn[i]+1), 0)
          
        global total
        total+= cur
        return
    elif(direction=='R'):
        return
    
    mn1= json.loads(json.dumps(mn))
    mx1= json.loads(json.dumps(mx))

    for rule in inp[direction]:
        if(':' in rule):
            dest= rule[rule.index(':')+1 :]
            val= int(rule[2:rule.index(':')]) 
            var= rule[0]

            if(rule[1]=='>'):
                prev=mn1[var]

                if(mn1[var]>val):
                    pass
                else:
                    mn1[var]= val+1
                
                check(dest, mn1, mx1)
                mn1[var]=prev
                mx1[var]=val

            else:
                prev=mx1[var]

                if(mx1[var]<val):
                    pass
                else:
                    mx1[var]=val-1

                check(dest, mn1, mx1)
                mn1[var]=val
                mx1[var]=prev
        else:
            check(rule, mn1, mx1)
            return
        


mn={}
mx={}
for i in "xmas":
    mx[i]=4000
    mn[i]=1

check("in", mn, mx)
print(total)
    
