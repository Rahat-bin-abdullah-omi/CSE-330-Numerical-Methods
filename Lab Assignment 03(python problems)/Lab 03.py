#!/usr/bin/env python
# coding: utf-8

# In[1]:


#problem-1:

a="Hello world"
print(a)


# In[4]:


#Problem-2:

x=4
if x%2!=0:
    print("weird")
else:
    if x >= 2 and x <= 5:
        print ("Not Weird")
    elif x >= 6 and x <= 20:
        print ("Weird")
    elif x > 20:
        print ("Not Weird")


# In[6]:


#Problem-3:

x=int (input(" Give Me Inputs: "))
for c in range(x):
    print (c**2)


# In[4]:


#Problem-4:


S=(input("Please Give Inputs : "))
num=[]
evenNum=[]
oddNum=[]
letter=[]
upperC=[]
lowerC=[]



for i in range(0,len(S)):
    if(    ord(S[i])<ord("A")    ):
        if(int(S[i])%2==0):
            evenNum.append(S[i])
        else:
            oddNum.append(S[i])

#print(evenNum)
#print(oddNum)
for i in  S:

    if(ord(i)>=97 and ord(i)<=122):
        lowerC.append(i)    
    if(ord(i)>=65 and ord(i)<=90):
        upperC.append(i)  
#print(lowerC)
#print(upperC) 

oddNum.sort()
evenNum.sort()

lowerC.sort()         
upperC.sort()

ans="".join(lowerC)
ans=ans +"".join(upperC)
ans=ans +"".join(oddNum)
ans=ans +"".join(evenNum)
print(ans)


# In[4]:


#Problen:-5

from datetime import datetime
for _ in range(int(input())):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print (int(abs((t1-t2).total_seconds())))


# In[2]:


#Problem-:6

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False

    return leap

if __name__ == '__main__':
    print(is_leap(int(input("Inter Year "))))


# In[3]:


#Problem-:7

def palindrome(N):
    for i in range(1, N + 1):
        print(int('1' * i)**2)

palindrome(int(input("Give Inputs: ")))


# In[7]:


#Problem-8:

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = (input("Please Give Inputs : "))

    occu_dict = {}
    for i in range(len(s)):
        if s[i] in occu_dict:
            occu_dict[s[i]] = (s[i], occu_dict[s[i]][1]+1)
        else:
            occu_dict[s[i]] = (s[i], 1)

    order_dict = sorted(occu_dict.values(), key=lambda x:(-x[1],x[0]))

    print('\n'.join(list(map(lambda x: x[0]+' '+str(x[1]), order_dict[:3]))))


# In[ ]:


#Problem-:9

n=int(input("Give Inputs : "))
arr=[[input(),float(input())] for _ in range(0,n)]
arr.sort(key=lambda x: (x[1],x[0]))
names = [i[0] for i in arr]
marks = [i[1] for i in arr]
min_val=min(marks)
while marks[0]==min_val:
    marks.remove(marks[0])
    names.remove(names[0])    
for x in range(0,len(marks)):
    if marks[x]==min(marks):
        print(names[x])







