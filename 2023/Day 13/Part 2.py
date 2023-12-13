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

inp=[]
inp= s.split('\n')


tempro=[]

lol=[]

for i in inp:
    # print(i, len(i), tempro)
    if(len(i)>0):
        tempro.append(i)
    else:
        lol.append(tempro.copy())
        tempro.clear()

lol.append(tempro)

# print(lol)

answer=0

for f in lol:
    arr=f


    n= len(arr)

    m=len(arr[0])

    old_row=[]
    old_col=[]


    for i in range(0,n-1):

        t=i
        b=i+1
        flag=0
        while (t>=0 and b<n):
            for j in range(m):
                if(arr[t][j]!= arr[b][j]):
                    flag=1
                    break

            if(flag==1):
                break
            else:
                t-=1
                b+=1

        if(flag==0):
            old_row.append(i+1)


    for i in range(0,m-1):

        l=i
        r=i+1
        flag=0
        while (l>=0 and r<m):
            for j in range(n):
                if(arr[j][l]!= arr[j][r]):
                    flag=1
                    break

            if(flag==1):
                break
            else:
                l-=1
                r+=1

        if(flag==0):
            old_col.append(i+1)


    for u in range(n):
        arr[u]=list(arr[u])




    row=[]
    col=[]
    # print(old_row, old_col)


    for u in range(n):
        for v in range(m):

            arr[u][v]= ('.' if arr[u][v]=='#' else '#')


            for i in range(0,n-1):

                t=i
                b=i+1
                flag=0
                while (t>=0 and b<n):
                    for j in range(m):
                        if(arr[t][j]!= arr[b][j]):
                            flag=1
                            break

                    if(flag==1):
                        break
                    else:
                        t-=1
                        b+=1

                if(flag==0):
                    if((i+1) not in old_row and (i+1) not in row):
                        row.append(i+1)
                        break


            for i in range(0,m-1):

                l=i
                r=i+1
                flag=0
                while (l>=0 and r<m):
                    for j in range(n):
                        if(arr[j][l]!= arr[j][r]):
                            flag=1
                            break

                    if(flag==1):
                        break
                    else:
                        l-=1
                        r+=1

                if(flag==0):
                    if((i+1) not in old_col and (i+1) not in col):
                        col.append(i+1)

            # print(u, v)
            # print(row,col, arr)
            arr[u][v]= ('.' if arr[u][v]=='#' else '#')


    answer+= (sum(row)*100 + sum(col))



print(answer)
