#!/usr/bin/env python
# coding: utf-8

# In[58]:


import csv
import matplotlib.pyplot as plt


# In[59]:


'''
next() 는 두가지 포맷으로 사용된다.
function 구조로 사용되면 header 만 리턴한다.
consumer 구조로 사용되면 data에서 header 를 제거한다.
row[날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)] 최고기온은 -1 이다.
data : [] = list() 는 list 타입의 data 를 list() 로 초기화 시키는 것이다.
단, 한 메소드 내에서만 사용하면 로컬에서 초기화한다. 예제는 다음과 같다. 
data : [] = None
def save_highest_temperatures(self):
     data = list()
그러나, 여러 메소드에서 사용하면 필드에서 초기화한다. 예제는 다음과 같다. 
data : [] = list()
'''


# In[60]:


data = csv.reader(open('../data/seoul.csv','rt', encoding='utf-8'))


# In[61]:


next(data)


# In[62]:


ls = list(data)


# In[63]:


#print([i for i in ls])


# In[64]:


#print([i[-1] for i in ls]) #show_highest_temperature


# In[65]:


highest_temperatures = []
[highest_temperatures.append(float(i[-1]))for i in ls if i[-1]!='']
print(f'총 {len(highest_temperatures)}')


# In[66]:


plt.figure(figsize=(10,2))
plt.plot(highest_temperatures,'r')


# In[67]:


high = [] # highest_temperature
low = [] # lowest_temperature


# In[68]:


for i in ls:
    if i[-1] != ''and i[-2] != '':
        if 1983 <= int(i[0].split('-')[0]):
            if i[0].split('-')[1] == '02' and i[0].split('-')[2]=='14':
                high.append(float(i[-1]))
                low.append(float(i[-2]))


# In[69]:


plt.rcParams['axes.unicode_minus'] = False
plt.title('Temperature change graph of My Birthday')
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.plot(high,'lightpink', label = 'high')
plt.plot(low, 'skyblue', label = 'low')
plt.legend()

