#!/usr/bin/env python
# coding: utf-8

# In[58]:


import csv
import matplotlib.pyplot as plt
import numpy as np


# In[59]:


data = csv.reader(open('../data/202106_202106_Population.csv', 'rt', encoding='utf-8'))
next(data)
data: [] = list(data)


# In[60]:


# print([i for i in data])


# In[61]:


home = []
name = "필동" # input()
[home.append(int(j)) for i in data if name in i[0] for j in i[3:]]
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.plot(home)
plt.show()


# In[62]:


mn = 1
home = []
result = 0
for i in data:
    if name in i[0]:
        home = np.array(i[3:], dtype=int)/int(i[2])
for i in data:
    away = np.array(i[3:], dtype=int) / int(i[2])
    s = np.sum((home - away) ** 2)
    if s < mn and name not in i[0]:
        mn = s
        result_name = i[0]
        result = away
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.title('similar_two_cities')
plt.plot(home, label='a')
plt.plot(away, label='b')
plt.show()


# In[ ]:





# In[ ]:




