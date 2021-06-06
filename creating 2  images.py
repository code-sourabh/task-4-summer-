#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


import numpy as np


# In[ ]:


# this is image 1


# In[ ]:


list_3d = []
for j in range(256):
    list_2d = []
    for i in range(256):
        list_2d.append([i,j,0])
    list_3d.append(list_2d)


# In[ ]:


array1 = np.array(list_3d)
array1 = array1.astype(np.uint8)


# In[ ]:


cv2.imshow('imgg' , array1)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[ ]:


# this is image 2 


# In[ ]:


list_3d = []
for j in range(300):
    list_2d = []
    for i in range(300):
        list_2d.append([i,j,255])
    list_3d.append(list2)


# In[ ]:


array2 = np.array(list_3d)
array2 = array2.astype(np.uint8)


# In[ ]:


cv2.imshow('imgg' , array2)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[ ]:




