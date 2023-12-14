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

now=0
seen= set()

find_dup = []

start=-1


while True:

    
    lol = temp.copy()

    for i in range(n):
        lol[i]= tuple(lol[i])

    lol=tuple(lol)

    if(lol in seen):
        start= find_dup.index(lol)
        break
    else:
        seen.add(lol)
        find_dup.append(lol)

    now+=1



    for i in range(m):
        cnt=0
        lol=[]
        for j in range(n-1, -1, -1):

            if(temp[j][i]=='O'):
                cnt+=1
            elif(temp[j][i]=='#' and cnt>0):
                for k in range(j+1, n):
                    if((temp[k][i]=='O' or temp[k][i]=='.') and cnt>0):
                        cnt-=1
                        temp[k][i]='O'
                    elif(temp[k][i]=='#'):
                        break
                    else:
                        temp[k][i]='.'
                    
                cnt=0


        if(cnt>0):
            for j in range(n):
                if((temp[j][i]=='O' or temp[j][i]=='.') and cnt>0):
                    cnt-=1

                    temp[j][i]='O'
                elif(temp[j][i]=='#'):
                    break
                else:
                    temp[j][i]='.'

    for i in range(n):
        cnt=0
        lol=[]
        for j in range(m-1, -1, -1):

            if(temp[i][j]=='O'):
                cnt+=1
            elif(temp[i][j]=='#' and cnt>0):
                for k in range(j+1, m):
                    if((temp[i][k]=='O' or temp[i][k]=='.') and cnt>0):
                        cnt-=1
                        temp[i][k]='O'
                    elif(temp[i][k]=='#'):
                        break
                    else:
                        temp[i][k]='.'
                    
                cnt=0


        if(cnt>0):
            for j in range(m):
                if((temp[i][j]=='O' or temp[i][j]=='.') and cnt>0):
                    cnt-=1
                    temp[i][j]='O'
                elif(temp[i][j]=='#'):
                    break
                else:
                    temp[i][j]='.'

        
    for i in range(m):
        cnt=0
        lol=[]
        for j in range(n):

            if(temp[j][i]=='O'):
                cnt+=1
            elif(temp[j][i]=='#' and cnt>0):
                for k in range(j-1, -1, -1):
                    if((temp[k][i]=='O' or temp[k][i]=='.') and cnt>0):
                        cnt-=1
                        temp[k][i]='O'
                    elif(temp[k][i]=='#'):
                        break
                    else:
                        temp[k][i]='.'
                    
                cnt=0


        if(cnt>0):
            for j in range(n-1, -1, -1):
                if((temp[j][i]=='O' or temp[j][i]=='.') and cnt>0):
                    cnt-=1

                    temp[j][i]='O'
                elif(temp[j][i]=='#'):
                    break
                else:
                    temp[j][i]='.'
    
    for i in range(n):
        cnt=0
        lol=[]
        for j in range(m):

            if(temp[i][j]=='O'):
                cnt+=1
            elif(temp[i][j]=='#' and cnt>0):
                for k in range(j-1, -1, -1):
                    if((temp[i][k]=='O' or temp[i][k]=='.') and cnt>0):
                        cnt-=1
                        temp[i][k]='O'
                    elif(temp[i][k]=='#'):
                        break
                    else:
                        temp[i][k]='.'
                    
                cnt=0


        if(cnt>0):
            for j in range(m-1, -1, -1):
                if((temp[i][j]=='O' or temp[i][j]=='.') and cnt>0):
                    cnt-=1
                    temp[i][j]='O'
                elif(temp[i][j]=='#'):
                    break
                else:
                    temp[i][j]='.'
    

rem= now-start 

left = 1000000000 - start

print(left%rem + (start))
temp= find_dup[left%rem + start]
for i in range(n):
    for j in range(m):
        if(temp[i][j]=='O'):
            ans.append((n-i))
            

print(sum(ans))
