#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 


# In[4]:


def backward_propagation(Z1, A1, Z2, A2, Z3, A3, W1, W2, W3, X, Y):
    m= X.shape()
    result ={
        
        "dZ3" : A3 - Y ,
        "dW3" : (1 / m) * np.dot(dZ3, A2.T),
        "db3" : (1 / m) * np.sum(dZ3, axis=1, keepdims=True),
    
        "dA2" : np.dot(W3.T, dZ3),
        "dZ2" : dA2 * (1 - np.power(A2, 2)),
        "dW2" : (1 / m) * np.dot(dZ2, A1.T),
        "db2" : (1 / m) * np.sum(dZ2, axis=1, keepdims=True),

        "dA1" : np.dot(W2.T, dZ2),
        "dZ1": dA1 * (1 - np.power(A1, 2)),
        "dW1" : (1 / m) * np.dot(dZ1, X.T),
        "db1" : (1 / m) * np.sum(dZ1, axis=1, keepdims=True),
    }
    
    return result 


# In[8]:


def update_params(W1, b1, W2, b2,W3,b3,dW1, db1, dW2, db2, dW3, db3,alpha):
    result={
        "W1": W1 -aplha*dW1,
        "W2": W2 -aplha*dW2,
        "W3": W3 -aplha*dW3,
        "b1": b1 -alpha*db1,
        "b2": b2 -alpha*db2,
        "b3": b3 -alpha*db3
    }
    return result 
    


# In[20]:


def get_prediction(A3):
    A3_index = np.argmax(A3,axis=0)
    return A3_index 

def get_accuracy(predicted_labels,Y):
    correct = np.sum(predicted_labels == Y) # Or directly from np.mean
    accuracy = (correct / Y.size) * 100
    return accuracy

def print_labels(predicted_labels, Y):
    print("predicted_labels:",end="")
    print(predicted_labels)

    print("Y",end="")
    print(Y)


# In[31]:


def Softmax(Z):
    exp_Z = np.exp(Z)
    sum = np.sum(exp_Z)
    return exp_Z/sum

def gradient_descent(X_train,Y_train,alpha,iterations ):
    
    # Take random weight and bias term 
    W = np.random.rand(len(X_train),len(X_train))
    b = np.random.rand(len(X_train),1)
    
    m = X_train.shape[0]
    for i in range(iterations):
        # Forwad propagation (helps in backward propagation)
        Z = np.dot(W.T,X_train) + b 
        a = softmax(Z)
    
        # Backward propagation calculation
        dZ = a - Y_train 
        dW = np.dot(X_train.T, dZ)/m
        db = np.sum(dZ, axis=0)/m
        
        # Update 
        W = W -alpha*dW
        b = b -alpha*db
        
        if i%10 ==0:
            accuracy = np.mean(a==Y_train)
            print(f"The Accuracy after {i}th itration is {accuracy}")
            print(a)
            
    return W,b
    
    


# In[ ]:




