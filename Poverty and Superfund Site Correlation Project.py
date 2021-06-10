#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import pandas library

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn


# In[7]:


NJpov = pd.read_csv("poverty.csv")


# In[8]:


NJpov


# In[9]:


NJpov['Percent of pop in poverty']


# In[10]:


NJpov['Percent of pop in poverty'] == 6.7


# In[11]:


NJpov.loc[NJpov['Percent of pop in poverty'] == 6.7,:]


# In[12]:


NJpov_6 = NJpov.loc[NJpov['Percent of pop in poverty'] == 6.7,:]


# In[13]:


NJpov['Percent of pop in poverty'] >= 10


# In[14]:


NJpov_10 = NJpov.loc[NJpov['Percent of pop in poverty'] >= 10,:]


# In[15]:


NJpov_10


# In[16]:


sorted_NJpov_10 = NJpov_10.sort_values('Percent of pop in poverty', ascending = False)


# In[17]:


sorted_NJpov_10


# In[18]:


sorted_NJpov_10.iloc[0:3]


# In[22]:


sorted_NJpov_10.plot.barh(x = 'County', y = 'Percent of pop in poverty')


# In[19]:


SFS_NJ = pd.read_csv('Superfund_Sites_NJ.csv')


# In[27]:


SFS_NJ_Sorted = SFS_NJ.sort_values('County', ascending = True)


# In[34]:


SFS_NJ_Sorted


# In[40]:


SFS_NJ_CC = SFS_NJ_Sorted.groupby(['County']).size()


# In[44]:


SFS_NJ_CC


# In[43]:


SFS_NJ_CC_sorted = SFS_NJ_CC.sort_values(size, ascending = True)


# In[39]:


SFS_NJ_CC.plot.barh(x = 'size', y = 'County')


# In[53]:


### In the examples I was watching she was giving parameters for both x and y, but 
###this error and stackflow say that she shouldn't be able to do that?

sn.countplot(x = "County",y = "Percent of pop in poverty", data = NJpov)
plt.show()

