#!/usr/bin/env python
# coding: utf-8

# 4.2 swapping image

# In[1]:


import cv2
import numpy as np


# In[2]:


cat1 = cv2.imread('cat1.jpg')
cat2 = cv2.imread('cat2.jpg')


# In[3]:


c1 = cv2.rectangle(cat1 , (0,0),(180,132) , (0,0,255) , 3)


# In[4]:


c2 = cv2.rectangle(cat2 , (40,0) , (220,132) , (0,255,0) , 3)


# In[5]:


cat1 = cv2.imread('cat1.jpg')
cat2 = cv2.imread('cat2.jpg')


# In[6]:


cv2.imshow('cropped' , c1)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[7]:


cv2.imshow('cropped' , c2)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[8]:


c3 = cat1[0:132 , 0:180]
c4 = cat2[0:132 , 40:220]


# In[9]:


cat1[0:132 , 0:180] = c4
cat2[0:132 , 40:220] = c3


# In[10]:


cv2.imshow('cropped' , cat2)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[12]:


cv2.imshow('cropped' , cat1)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[ ]:




