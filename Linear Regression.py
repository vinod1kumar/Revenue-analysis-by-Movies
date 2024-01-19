#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt


# In[54]:


Data = pandas.read_csv('cleaning data.csv')


# In[57]:


Data.describe()


# In[58]:


x=DataFrame(Data,columns=['Production Budget'])
y=DataFrame(Data,columns=['Worldwide gross'])


# In[60]:


plt.scatter(x,y,alpha=0.3)
plt.title('Film budget VS Worldwide Collection')
plt.xlabel('Production Budget')
plt.ylabel('Worldwide gross')
plt.ylim(0,3000000000)
plt.xlim(0,45000000)
plt.show()


# In[ ]:




