#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


df= pd.read_csv(r"C:\Users\DELL\Desktop\DOT glasses.csv")


# In[3]:


print(df)


# In[4]:


df.head()


# In[7]:


df.tail()


# In[9]:


df.isnull()


# In[10]:


df.isnull().sum()


# In[ ]:




