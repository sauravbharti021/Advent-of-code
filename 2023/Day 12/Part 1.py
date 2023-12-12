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

n= len(arr)

mx=0

answers=[]
for i in arr:
    x=i.split(' ')
    mx=max(mx, len(x[0]))

    temp= x[1]
    nums=temp.split(',')

    
    for k in range(len(nums)):
        nums[k]= int(nums[k])

            
    st= x[0]
    a= nums
    
    @functools.cache
    def recur(l, r):

        # print(l,r)
        if(l>=len(st)):
            if(r>=len(a)):
                return 1
            return 0
        
        if(r>=len(a)):
            for k in range(l, len(st)):
                if(st[k]=='#'):
                    return 0
                
            return 1
        
        ans=0

        if(st[l]=='#'):
            if(l+a[r]>len(st)):
                return 0
            for k in range(l, l+a[r]):
                if(st[k]=='.'):
                    return 0
            
            if(l+a[r]<len(st) and st[l+a[r]]=='#'):
                return 0
                
            ans+= recur(l+a[r]+1, r+1)

        elif(st[l]=='?'):

            if(l+a[r]>len(st)):
                return 0
            
            flag=0
            if(l+a[r]<len(st) and st[l+a[r]]=='#'):
                flag=1
            
            for k in range(l, l+a[r]):
                if(st[k]=='.'):
                    flag=1
                    break
            
            if(flag==1):
                ans+= recur(l+1, r)
            else:
                ans+= recur(l+1, r) + recur(l+a[r]+1, r+1)

        else:
            ans+= recur(l+1, r)

        
        return ans
    
    # print(x[0], nums, recur(0, 0, x[0], nums))
    answers.append(recur(0, 0))


print(sum(answers))
