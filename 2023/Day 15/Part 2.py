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


arr= s.split(',')


def hash(st):
    cur=0
    for j in range(len(st)):
        cur+= (ord(st[j]))
        cur*= 17
        cur%= 256


    return cur


dic= collections.defaultdict(list)

for i in arr:
    m=len(i)
    st= i[:(m-2 if i[m-1]!='-' else m-1):]

    h= hash(st)

    
    if(i[m-1]=='-'):
        ind=[]
        for j in range(len(dic[h])):
            left= dic[h][j].split("->")
            if(left[0]==st):
                ind.append(j)

        for j in range(len(ind)-1, -1, -1):
            dic[h].pop(ind[j])

    else:
        lol= st+ '->'+ i[m-1]
        flag=0
        for j in range(len(dic[h])):
            left= dic[h][j].split("->")
            if(left[0]==st):
                dic[h][j] = lol
                flag=1
                break
        if(flag==0):
            dic[h].append(lol)



answer=[]

for i in range(0, 256):
    
    for j in range(len(dic[i])):
        cur=(i+1)
        left= dic[i][j].split("->")

        cur*= (j+1)
        cur*= (int(left[1]))

        answer.append(cur)

print(sum(answer))
