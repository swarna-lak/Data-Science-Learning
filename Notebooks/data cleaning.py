#!/usr/bin/env python
# coding: utf-8

# In[155]:


import pandas as pd 


# In[157]:


csv_data=pd.read_csv("C:/Users/ashak/OneDrive/Desktop/swarna/name.csv")
print(csv_data)


# In[159]:


json_data=pd.read_json("C:/Users/ashak/OneDrive/Desktop/swarna/city.json")
print(json_data)


# In[161]:


data=pd.concat([csv_data,json_data])
print(data)


# In[163]:


clean_data=data.dropna()
print(clean_data)


# In[165]:


clean_data.to_csv("C:/Users/ashak/OneDrive/Desktop/swarna/cleaned_data.csv",index=False)
print("cleaned data is exported")


# In[ ]:





# In[ ]:




