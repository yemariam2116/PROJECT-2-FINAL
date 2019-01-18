
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np


# In[23]:


Location = "datasets/DC_Properties.csv"
df = pd.read_csv(Location)

df.head()


# In[24]:


df.corr()


# In[5]:


import statsmodels.formula.api as smf


# In[20]:


result = smf.ols('PRICE ~ ROOMS + BATHRM + LANDAREA', data=df).fit()


# In[13]:


result.summary()


# In[25]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

get_ipython().magic('matplotlib inline')


# In[26]:


df = pd.read_csv("datasets/DC_Properties.csv", encoding = "ISO-8859-1") 
df.head()


# In[27]:


sns.lmplot(x='ROOMS', y='PRICE', data=df)


# In[ ]:


sns.violinplot(x='LANDAREA', y='PRICE', data=df)

