#!/usr/bin/env python
# coding: utf-8

# # Ecommerce Purchases

# In[ ]:


import pandas as pd
import pandas as pd
import numpy as 


# In[88]:


data= pd.read_csv("C:/Users/akanksha/Desktop/Ecommerce Purchases.csv")


# In[89]:


data


# Display Top 5 Rows of the Dataset

# In[90]:


data.head()


# Dispaly Last 5 Rows the Dataset

# In[91]:


data.tail()


# # check datatype of each column

# In[92]:


data.dtypes


# # check Null values in the dataset

# In[93]:


data.isnull().sum()


# # how many rows and columns are there in our dataset

# In[94]:


data.columns


# In[95]:


len(data.columns)


# In[96]:


len(data)


# In[99]:


data.info()


# # Highest and lowest purches prices

# In[42]:


data.columns


# In[43]:


data["Purchase Price"].max()


# In[44]:


data["Purchase Price"].min()


# In[ ]:





# # Average Purchase price

# In[45]:


data["Purchase Price"].mean()


# # How many people french "fr" AS their language

# In[46]:


data.columns


# In[47]:


data["Language"] =='fr'


# In[48]:


data[data["Language"] =='fr']


# In[49]:


len(data[data["Language"] =='fr'])


# In[50]:


data[data["Language"] =='fr'].count()


# # job title contains engineer

# In[51]:


data['Job']


# In[52]:


data['Job'].str.contains("engineer")


# In[53]:


data[data['Job'].str.contains("engineer",case=False)]


# In[54]:


len(data[data['Job'].str.contains("engineer",case=False)]) ## 984 job title in engnieer


# # Find email of the person with the following IP address:242.8.85.205

# In[59]:


data[data['IP Address']=="242.8.85.205"]["Email"]


# # How many people have manstercard as their credit card provider and made a purchase avobe 5o?

# In[60]:


data["CC Provider"]


# In[62]:


data[(data["CC Provider"]=="Mastercard") & (data["Purchase Price"]>50)]


# In[63]:


len(data[(data["CC Provider"]=="Mastercard") & (data["Purchase Price"]>50)])


# In[64]:


data[(data["CC Provider"]=="Mastercard") & (data["Purchase Price"]>50)].count()


# # Find Email of the person with the following credit card Number:

# In[66]:


data[data["Credit Card"]==6011508474487291]["Email"]


# # How many people purchase during the AM and how many people purchase during PM

# In[67]:


data["AM or PM"].value_counts()


# # how many people have a credit card that  expries in  2020

# In[68]:


data["CC Exp Date"]


# In[69]:


def fun():
    count=0
    for date in data["CC Exp Date"]:
        if date.split('/')[1]=='20':
            count=count+1
    print(count)


# In[70]:


fun()


# In[72]:


data[data["CC Exp Date"].apply(lambda x:x[3:]=='20')]


# In[73]:


len(data[data["CC Exp Date"].apply(lambda x:x[3:]=='20')])


# # Top 5 most popular email providers (e.g gmail.com, yahoo.com,etc....

# In[74]:


list1=[]
for email in data["Email"]:
    email.split("@")


# In[75]:


data['Email']


# In[76]:


list1=[]
for email in data["Email"]:
    list1.append(email.split("@")[1])


# In[77]:


data["temp"]=list1


# In[79]:


data.head(1)


# In[80]:


data["temp"].value_counts().head()


# In[ ]:





# In[ ]:




