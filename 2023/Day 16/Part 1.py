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


arr= s.split('\n')

n= len(arr)
m= len(arr[0])

q= collections.deque()
q.append(( (0, 0), 'E' ))

st= set()



while len(q)>0:
    ((x,y), d)= q.popleft()

    while True:
        if(y<0 or x<0 or y>=m or x>=n):
            break


        if(((x,y), d) in st):
                break
        else:
            st.add(((x,y), d))

        if(d=='E'):
            

            if(arr[x][y]=='.' or arr[x][y]=='-'):
                y+=1
            elif(arr[x][y]=='|'):
                if(x-1>=0):
                    q.append(((x-1, y), 'N'))
                if(x+1<n):
                    q.append(((x+1, y), 'S'))
                break
            elif(arr[x][y]== '\\'):
                if(x+1<n):
                    q.append(((x+1, y), 'S'))
                break
            elif(arr[x][y]=='/'):
                if(x-1>=0):
                    q.append(((x-1,y), 'N'))
                break


        if(d=='W'):

            if(arr[x][y]=='.' or arr[x][y]=='-'):
                y-=1
            elif(arr[x][y]=='|'):
                if(x-1>=0):
                    q.append(((x-1, y), 'N'))
                if(x+1<n):
                    q.append(((x+1, y), 'S'))
                break
            elif(arr[x][y]== '\\'):
                if(x-1>=0):
                    q.append(((x-1,y), 'N'))
                
                break
            elif(arr[x][y]=='/'):
                if(x+1<n):
                    q.append(((x+1, y), 'S'))
                break        

        
        if(d=='N'):
            if(arr[x][y]=='.' or arr[x][y]=='|'):
                x-=1
            elif(arr[x][y]=='-'):
                if(y-1>=0):
                    q.append(((x, y-1), 'W'))
                if(y+1<m):
                    q.append(((x, y+1), 'E'))
                break
            elif(arr[x][y]== '\\'):
                if(y-1>=0):
                    q.append(((x,y-1), 'W'))
                
                break
            elif(arr[x][y]=='/'):
                if(y+1<m):
                    q.append(((x, y+1), 'E'))
                break 

        if(d=='S'):
            if(arr[x][y]=='.' or arr[x][y]=='|'):
                x+=1
            elif(arr[x][y]=='-'):
                if(y-1>=0):
                    q.append(((x, y-1), 'W'))
                if(y+1<m):
                    q.append(((x, y+1), 'E'))
                break
            elif(arr[x][y]== '\\'):
                if(y+1<m):
                    q.append(((x, y+1), 'E'))
                
                
                break
            elif(arr[x][y]=='/'):
                if(y-1>=0):
                    q.append(((x,y-1), 'W'))
                break



answer = set()
for ((x,y),d) in st:
    answer.add((x,y))

print(len(answer))
