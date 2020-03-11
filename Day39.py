#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
from io import StringIO

# In[2]:


data = ('col1, col2, col3\n'
        'a,b,1\n'
        'a,b,2\n'
        'c,d,3')
pd.read_csv(StringIO(data))


# In[3]:


pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['COL1', 'COL3'])


# In[5]:


data = ('col1, col2, col3\n'
        'a,b,1\n'
        'a,b,2\n'
        'c,d,3')


# In[6]:


pd.read_csv(StringIO(data))


# In[7]:


pd.read_csv(StringIO(data), skiprows=lambda x: x % 2 != 0)


# In[8]:


data = ('a,b,c,d\n'
        '1,2,3,4\n'
        '5,6,7,8\n'
        '9,10,11')


# In[9]:


print(data)


# In[10]:


df = pd.read_csv(StringIO(data), dtype=object)


# In[11]:


df


# In[12]:


df['a'][0]


# In[14]:


import numpy as np
df = pd.read_csv(StringIO(data),dtype={'b': object, 'c': np.float64, 'd': 'Int64'})


# In[15]:


df.dtypes


# In[16]:


data = ("col_1\n"
        "1\n"
        "2\n"
        "'A'\n"
        "4.22")


# In[17]:


df = pd.read_csv(StringIO(data), converters={'col_1': str})


# In[18]:


df


# In[19]:


df['col_1'].apply(type).value_counts()


# In[20]:


df2 = pd.read_csv(StringIO(data))


# In[21]:


df2['col_1'] = pd.to_numeric(df2['col_1'], errors='coerce')


# In[22]:


df2


# In[23]:


df2['col_1'].apply(type).value_counts()


# In[24]:


col_1 = list(range(500000)) + ['a', 'b'] + list(range(500000))


# In[25]:


df = pd.DataFrame({'col_1': col_1})


# In[26]:


df.to_csv('foo.csv')


# In[27]:


mixed_df = pd.read_csv('foo.csv')


# In[28]:


mixed_df['col_1'].apply(type).value_counts()


# In[29]:


mixed_df['col_1'].dtype


# In[30]:
df = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',
                 sep='\t')
# In[32]:
data = [{'id': 1, 'name': {'first': 'Coleen', 'last': 'Volk'}},
        {'name': {'given': 'Mose', 'family': 'Regner'}},
        {'id': 2, 'name': 'Faye Raker'}]
# In[34]:
import matplotlib.pyplot as plt
plt.close('all')
# In[35]:
ts = pd.Series(np.random.randn(1000),
index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
# In[39]:
df = pd.DataFrame(np.random.randn(1000, 4),
index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure();
df.plot();
# In[40]:

df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
df3.plot(x='A', y='B')
# In[41]:
plt.figure();
df.iloc[5].plot(kind='bar');
# In[44]:
plt.figure();
df.iloc[5].plot.bar()
plt.axhline(0, color='k');
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot.bar();
df2.plot.bar(stacked=True)


# In[47]:


df2.plot.barh(stacked=True)


# In[48]:


df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),
                       'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
   

plt.figure();

df4.plot.hist(alpha=0.5)


# In[51]:


plt.figure()

df4.plot.hist(stacked=True, bins=20)


# In[52]:


plt.figure();

df4['a'].plot.hist(orientation='horizontal', cumulative=True)


# In[53]:


plt.figure();

df['A'].diff().hist()


# In[54]:


plt.figure()
df.diff().hist(color='k', alpha=0.5, bins=50)


# In[55]:


data = pd.Series(np.random.randn(1000))

data.hist(by=np.random.randint(0, 4, 1000), figsize=(6, 4))


# In[56]:


df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box()


# In[57]:


color = {'boxes': 'DarkGreen', 'whiskers': 'DarkOrange',
             'medians': 'DarkBlue', 'caps': 'Gray'}
df.plot.box(color=color, sym='r+')


# In[58]:


df.plot.box(vert=False, positions=[1, 4, 5, 6, 8])


# In[59]:


df = pd.DataFrame(np.random.rand(10, 5))
plt.figure();
bp = df.boxplot()


# In[60]:


df = pd.DataFrame(np.random.rand(10, 2), columns=['Col1', 'Col2'])
df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
plt.figure()
bp = df.boxplot(by='X')


# In[61]:


df = pd.DataFrame(np.random.rand(10, 3), columns=['Col1', 'Col2', 'Col3'])
df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
df['Y'] = pd.Series(['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'])
plt.figure()
bp = df.boxplot(column=['Col1', 'Col2'], by=['X', 'Y'])


# In[62]:


np.random.seed(1234)
df_box = pd.DataFrame(np.random.randn(50, 2))
df_box['g'] = np.random.choice(['A', 'B'], size=50)
df_box.loc[df_box['g'] == 'B', 1] += 3
bp = df_box.boxplot(by='g')


# In[63]:


bp = df_box.groupby('g').boxplot()


# In[64]:


df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area()


# In[65]:


df.plot.area(stacked=False)


# In[66]:


df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b');


# In[ ]:




