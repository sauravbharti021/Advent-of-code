
import math
import collections


path = "C:\\Users\\saura\\Desktop\\PROJECT\\scaler\\input.txt"

s="" 
try:
    with open(path) as file:
        s=(file.read())
except Exception as e:
    print(e)

arr=[]
arr= s.split('\n')

n=len(arr)

inp= []


for i in range(n):
    lol= arr[i]
    temp=lol.split('~')
    print(temp)

    prev= temp[0].split(',')
    next= temp[1].split(',')
    t=[]
    for j in prev:
        t.append(int(j))
    for j in next:
        t.append(int(j))
    inp.append(t)



print(inp)

inp.sort( key= lambda x: x[2])
child=collections.defaultdict(list)
parent= collections.defaultdict(list)

for i in range(n):
    
    mx=0
    x1,y1,z1= inp[i][0], inp[i][1], inp[i][2]
    x2, y2, z2 = inp[i][3], inp[i][4], inp[i][5]

    for j in range(i-1, -1,-1):
        l1,r1,k1= inp[j][0], inp[j][1], inp[j][2]
        l2, r2, k2 = inp[j][3], inp[j][4], inp[j][5]

        if(z1>k2):
            for le in range(l1, l2+1):
                for ri in range(r1, r2+1):
                    if(le>=x1 and le<=x2 and ri>=y1 and ri<=y2):
                        mx=max(mx, k2)

    
    for j in range(i-1,-1,-1):

        l1,r1,k1= inp[j][0], inp[j][1], inp[j][2]
        l2, r2, k2 = inp[j][3], inp[j][4], inp[j][5]

        if(k2!=mx):
            continue
        flag=0

        for le in range(l1, l2+1):
            for ri in range(r1, r2+1):
                if(le>=x1 and le<=x2 and ri>=y1 and ri<=y2):
                    flag=1

        if(flag):
            parent[j].append(i)
            child[i].append(j)

    dis= inp[i][5]-inp[i][2]
    inp[i][2]=mx+1
    inp[i][5]=(inp[i][2]+dis)

cnt=0
print(child)
for i in range(n):
    if(i not in parent):
        cnt+=1
        continue
    key= parent[i]
    flag=0
    for j in key:
        if(len(child[j])==1):
            flag=1

    if (not flag):
        cnt+=1


print(cnt)
    


