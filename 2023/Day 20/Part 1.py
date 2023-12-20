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
index=-1

nd= []
pt=[]

dest=collections.defaultdict(list)



casters=list()


for i in range(n):
    lol=arr[i]

    temp=lol.split('->')
    for j in range(len(temp)):
        temp[j]= temp[j].strip()

    
    if(temp[0]=="broadcaster"):
        lol= temp[1].split(',')
        for j in lol:
            j=j.strip()
            casters.append(j)

    else:
        if(temp[0][0]=='%'):
            pt.append(temp[0][1::])
            if(',' in temp[1]):
                places= temp[1].split(',')
                for j in places:
                    j=j.strip()
                    dest[temp[0][1::]].append(j)
            else:
                dest[temp[0][1::]].append(temp[1])

        else:
            nd.append(temp[0][1::])
            if(',' in temp[1]):
                places= temp[1].split(',')
                for j in places:
                    j=j.strip()
                    dest[temp[0][1::]].append(j)
            else:
                dest[temp[0][1::]].append(temp[1])


pulse_r= {}
for_inp= collections.defaultdict(list)

for i in pt:
    for j in nd:
        if(j in dest[i]):
            for_inp[j].append(i)
            pulse_r[(j, i)]= "low"


vals=dict()
for i in pt:
    vals[i]='off'



cnt=0
l,h=1000,0

while cnt<1000:
    q= collections.deque()

    receivers= collections.defaultdict(list)

    for i in casters:
        q.append(("broadcaster", "low", i))
    

    

    while(len(q)>0):



        size=len(q)
        while (size)>0:
            
            (prev, value, x)= q.popleft()

            # print(prev, value, x)

            if(value=="low"): l+=1 
            else: h+=1

            flag=0
            if(x in nd):
                flag=1
                pulse_r[(x, prev)]=value


            for j in dest[x]:
                if not flag:
                    if(value=="low"):
                        if(vals[x]=='off'):
                            q.append((x, "high", j))
                        else:
                            q.append((x, "low", j))
                    


                else:
                    flag2=0
                    
                    for lef, rig in pulse_r.items():
                        (left, right)=lef
                        if(left==x and rig=="low"):
                            flag2=1

                    if(flag2):
                        q.append((x, "high", j))
                    else:
                        q.append((x, "low",j))

            if not flag:
                if(value=="low" and x in pt):
                    if(vals[x]=="off"):
                        vals[x]="on"
                    else:
                        vals[x]="off"
                
            size-=1
    
    cnt+=1


print((l*h))

