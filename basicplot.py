#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[4]:


def plot_show():
    plt.title('color')
    plt.plot([10, 20, 30, 40], color ='skyblue', linestyle = ':', label='asc')
    plt.plot([40, 30, 20, 10], 'pink', ls='--', label='desc')
    plt.plot([50, 20, 40, 60], 'y:', label='dashed')
    plt.legend()
    plt.show()


# In[5]:


plot_show()


# In[8]:


def plot_two_list_show():
    plt.plot([1,2,3,4], [12,43,25,15])
    plt.show()


# In[9]:


plot_two_list_show()


# In[10]:


def scatter():
    plt.title('marker')
    plt.plot([10, 20, 30, 40], 'r.', label='circle')
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
    plt.plot([50, 20, 10, 60], 'y:', label='dashed')
    plt.legend()
    plt.show()


# In[11]:


scatter()


# In[ ]:




