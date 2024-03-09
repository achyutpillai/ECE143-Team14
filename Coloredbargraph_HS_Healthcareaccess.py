#!/usr/bin/env python
# coding: utf-8

# In[4]:


#pip install pivottablejs
import pandas as pd
import matplotlib.pyplot as plt
from pivottablejs import pivot_ui

plt.figure(figsize=(25, 12))
# Load the dataset into a DataFrame
data =pd.read_csv(r"C:\Users\riyaj\Downloads\__hap.csv",skipfooter=1, engine='python') 
print("Shape before removing null values:", data.shape)

# Remove rows with any null values
data = data.dropna()

# Display the shape of the DataFrame after removing null values
print("Shape after removing null values:", data.shape)

# Create a pivot table using the pivot_ui function
pivot_ui(data)


# In[ ]:




