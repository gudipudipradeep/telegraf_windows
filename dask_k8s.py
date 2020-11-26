#!/usr/bin/env python
# coding: utf-8

# In[14]:


from dask.distributed import Client


# In[15]:


from dask_kubernetes import KubeCluster


# In[16]:


cluster = KubeCluster.from_yaml("worker-spec.yml")
cluster.scale(1) 


# In[13]:


cluster.close()


# In[ ]:




