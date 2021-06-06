#!/usr/bin/env python
# coding: utf-8

# In[1]:


# making collage of multiple images.


# In[3]:


import cv2 
import numpy as np


# In[4]:


list_3d = []
for j in range(256):
    list_2d = []
    for i in range(256):
        list_2d.append([i,j,0])
    list_3d.append(list_2d)
    
array1 = np.array(list_3d)
array1 = array1.astype(np.uint8)

cv2.imshow('imgg' , array1)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[9]:


list_3d = []
for j in range(256):
    list_2d = []
    for i in range(256):
        list_2d.append([i,j,255])
    list_3d.append(list_2d)
    
array2 = np.array(list_3d)
array2 = array2.astype(np.uint8)

cv2.imshow('imgg' , array2)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[12]:


collage = np.append(array1 , array2 , axis = 0)


# In[13]:


cv2.imshow('imgg' , collage)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[ ]:





# In[14]:


cat1 = cv2.imread('cat1.jpg')
cat2 = cv2.imread('cat2.jpg')


# In[17]:


cat1.shape
c3 = cat1[0:132 , 0:180]


# In[18]:


cat2.shape
c4 = cat2[0:132 , 40:220]


# In[21]:


collage2 = np.append(c3 , c4 , axis=0)


# In[22]:


cv2.imshow('imgg' , collage2)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




