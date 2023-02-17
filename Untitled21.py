#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Problem 1


# In[ ]:


#AList Contains the average daily temperature(in degree Celsius)of a city over a particularweek. Write a Python code to find the index of maximum and minimum Temperature


# In[7]:


# A List containing average daily temperature over a weak
my_list=[34 , 40 , 29 , 33 , 42, 37 , 39]


# In[8]:


max(my_list)


# In[12]:


my_list.index(42)


# In[13]:


min(my_list)


# In[14]:


my_list.index(29)


# In[ ]:


Problem 2


# In[ ]:


# Change the values of dictionary to river names


# In[29]:


city = ["Nepal" ,"Kathmandu", "England","London"]


# In[31]:


river = [ "Koshi","Trishuli", "River Thames" ,"River Fleet"]


# In[32]:


city_river=list(zip(city,river))


# In[33]:


city_river


# In[34]:


dict(city_river)


# In[ ]:




