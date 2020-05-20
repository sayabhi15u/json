#!/usr/bin/env python
# coding: utf-8

# In[27]:


def duplicates(dc,pf):
    global paid
    global free
    if pf=='paid':
        if dc in paid:
            return 1
        else:
            return 0
    if pf=='free':
        if dc in free:
            return 1
        else:
            return 0


# In[28]:


def printer(dc):
    print(f"\"{dc['confName']}\",{dc['confStartDate']},{dc['city']} {dc['state']},{dc['country']},{dc['entryType']}")


# In[29]:


import requests
import json


# In[33]:



try:
    r=requests.get('https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')
    print(r.status_code)
except Exception as e:
    print("Error"+"\n"+e)


# In[45]:


output=json.loads(r.text)
output=json.dumps(output,sort_keys=True)
output=json.loads(output)


# In[46]:


for i in output['paid']:
    paid=[]
free=[]
dp=[]
for i in output['paid']:
    printer(i)
    i.pop('confName')
    if duplicates(i,'paid')==0:
        paid.append(i)
    else:
        dp.append(i)
for i in output['free']:
    printer(i)
    i.pop('confName')
    if duplicates(i,'free')==0:
        paid.append(i)
    else:
        dp.append(i)
print(dp)

