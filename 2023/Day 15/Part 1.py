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

ans=[]

for i in arr:

    cur=0
    for j in range(len(i)):
        cur+= (ord(i[j]))
        cur*= 17
        cur%= 256

    ans.append(cur)

print(sum(ans))
