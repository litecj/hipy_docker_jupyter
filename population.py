#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
import matplotlib.pyplot as plt
import numpy as np


# In[7]:


data: [] = list()
name:str = ''
name2 = ''
home = list()
away = None


# In[8]:


data = csv.reader(open('../data/202106_202106_Population.csv', 'rt', encoding='utf-8'))
next(data)
data = list(data)


# In[9]:


name = "필동"#input("어느동 ")
for i in data :
    if name in i[0]:
        home = np.array(i[3:], dtype=int)/int(i[2])
        name = i[0]


# In[13]:


mn = 1
for i in data:
    bar = np.array(i[3:], dtype=int)/int(i[2])
    s = np.sum(abs(home-bar))  # ((self.home-self.away)**2) / (abs(self.home-self.away))
    if s < mn and name not in i[0]:
        mn = s
        name2 = i[0]
        result = bar
away = result
print(name2)


# In[14]:


plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.title('similar_pop_per_dong')
plt.plot(home, label="pildong")
plt.plot(away, label="similar_dong")
plt.legend()
plt.show()


# In[ ]:




