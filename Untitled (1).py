#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 


# In[15]:


# Importing this data in current jupyter notebook
dataset = pd.read_csv('train.csv')


# In[17]:


# spliting the data 
X_dev = dataset.head(1001)
Y_dev = X_dev 

X_train = dataset.tail(40999)
Y_train = X_train 
X_train


# In[14]:


# Normalising the pixcel values 
X_dev = X_dev/255
X_train = X_train/255 
X_dev['label'] = X_dev['label']*255 
X_train['label'] = X_train['label']*255 
X_train


# In[ ]:




