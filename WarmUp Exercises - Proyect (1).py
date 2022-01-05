#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd


# In[84]:


dict1 ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female']
               }


# In[85]:


df1=pd.DataFrame(dict1)
df1


# In[9]:


df1.head(3)


# In[10]:


df1.tail(3)


# In[16]:


df1.shape


# In[18]:


print('Number of rows', df1.shape[0])
print('Number of columns', df1.shape[1])


# 

# In[19]:


df1.info()


# In[25]:


df1.isnull().sum(axis=1)


# In[27]:


df1.describe(include='all')


# In[28]:


df1


# In[30]:


df1['Gender'].unique()


# In[31]:


df1['Gender'].nunique()


# In[33]:


df1['Gender'].value_counts()


# In[38]:


df1[df1['Marks']>=90]


# In[39]:


len(df1[df1['Marks']>=90])


# In[42]:


df1[(df1['Marks']>=90) & (df1['Marks']<=100)]


# In[43]:


len(df1[(df1['Marks']>=90) & (df1['Marks']<=100)])


# In[45]:


df1[df1['Marks'].between(90,100)]


# In[46]:


len(df1[df1['Marks'].between(90,100)])


# In[47]:


df1


# In[50]:


df1['Marks'].mean()


# In[51]:


df1['Marks'].min()


# In[52]:


df1['Marks'].max()


# In[53]:


df1


# In[63]:


def marks(x):
    return x//2


# In[64]:


df1['Marks'].apply(marks)


# In[65]:


df1['Half_marks']=df1['Marks'].apply(marks)
df1


# In[68]:


df1['Marks'].apply(lambda x:x//2)


# In[69]:


df1


# In[70]:


df1['Name'].apply(len)


# In[71]:


df1


# In[89]:


df1['Male_Female']=df1['Gender'].map({'Male':1,'Female':0})
df1


# In[90]:


df1


# In[91]:


df1.drop('Male_Female',axis=1)


# In[95]:


df1.drop('Male_Female',axis=1,inplace=True)


# In[96]:


df1


# In[97]:


df1.columns


# In[98]:


df1.index


# In[99]:


df1


# In[102]:


df1.sort_values(by='Marks')


# In[103]:


df1.sort_values(by='Marks',ascending=False)


# In[105]:


df1.sort_values(by=['Marks','Gender'],ascending=False)


# In[106]:


df1


# In[113]:


df1[df1['Gender'] == 'Female'][['Name','Marks']]


# In[114]:


df1


# In[117]:


df1[df1['Gender'].isin(['Female'])][['Name','Marks']]


# In[ ]:




