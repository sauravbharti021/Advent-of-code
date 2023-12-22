
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
for i in range(n):
    tot=0
    
    
    st= set()
    def dfs(par):

        
        st.add(par)
        for k in parent[par]:
                flag1=0
                flag2=0
                if(len(child[k])==1 ):
                    flag1=1
                for l in child[k]:
                    if(l not in st):
                        flag2=1

                if(flag1 or (not flag2)):
                    dfs(k)


    flag=0
    for j in parent[i]:
        if(len(child[j])==1):
            flag=1
            dfs(j)

    if(flag):
        cnt+=len(st)
        



print(cnt)
    


