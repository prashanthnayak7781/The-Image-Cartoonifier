#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np 
import pandas as pd 


# In[21]:


def init_params(l1,l2):
    dictionary1 = {
        "w": np.random.rand(l2,l1 )  ,
        "b":np.random.rand(l2,1)
    }
    return dictionary1 
layers = [784,120,45,10] 

weights = {}   
bias = {}   
for i in range(1,len(layers)):
    
    
    weights[f'W{i}'] = np.random.rand(layers[i],layers[i-1])
    
    
    bias[f'B{i}'] = np.random.rand(layers[i],1)

weights[f'W{1}']


# In[15]:


def ReLU(Z):
    return np.maximum(0,Z)


# In[16]:


def Softmax(Z):
    exp_Z = np.exp(Z)
    sum = np.sum(exp_Z)
    return exp_Z/sum


# In[22]:


def forward_propagation(X,weights,bias):
    result = {
        "Z1": np.dot(weights[f'W{1}'],X) + bias[f'B{1}']
        "A1":ReLU(result[f'Z{1}'])
        "Z2": np.dot(weights[f'W{2}'],result[f'A{1}']) + bias[f'B{2}']
        "A2":ReLU(result[f'Z{2}'])
        "Z3": np.dot(weights[f'W{3}'],result[f'A{2}']) + bias[f'B{3}']
        "A3":ReLU(result[f'Z{3}'])
    }    
    return result 


# In[25]:


def one_hot(Y):
    l = len(Y)
    classes = np.max(Y) +1 
    matrix = np.zeros((classes,l),dtype =int)
    for i in range(0,l):
        matrix[Y[i]][i] = 1 
    return matrix.T 
        


# In[ ]:




