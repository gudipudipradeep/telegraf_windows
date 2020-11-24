#!/usr/bin/env python
# coding: utf-8

# In[82]:


from dask.distributed import Client

client = Client(n_workers=4)


# In[83]:


client


# In[84]:


from dask.distributed import wait, progress

def inc(x):
    return x + 1

total = client.map(inc, range(1,1000))
#progress(total)
gather_result = client.gather(total)
#print(total)

#fut = client.map(inc, range(0, 1000))
#print(progress(fut))


# In[85]:


print(gather_result)
client.close()


# In[ ]:




