#!/usr/bin/env python
# coding: utf-8

# In[2]:



station_names = ['lighthouse', 'Harmaja','Suomenlinna aaltopoiju', 'Kumpula' , 'Kaisaniemi']
station_start_years = ['2003', '1989' , '2016', '2005' , '1844']


# In[4]:


print(station_names)
print(station_start_years)


# In[5]:


len(station_names)


# In[9]:


station_names.append('Malmi airfield')
station_names.append('Vuosaari harbour') 
station_names.append('Kaivopuisto')
station_start_years.append('1937')
station_start_years.append('2012') 
station_start_years.append('1904')


# In[10]:


print(station_names)
print(station_start_years)


# In[13]:


station_names.sort()
print(station_names)


# In[19]:


station_start_years.sort()
station_start_years.reverse()
print(station_start_years)


# In[30]:


# This piece of code will input a list of months
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

# This piece of code defines the average monthly temperature of the months above
average_monthly_temperature = ['-3.5','-4.5','-1.0','4.0','10.0','15.0','18.0','16.0','11.5','6.0','2.0','-1.5']

# Use this piece of code to retrieve the information from the specific month  
selected_month_index=7

# This code outputs the statement based on your input month above and gives the average temperature that month
print("The average temperature in Helsinki in", months[selected_month_index],"is", average_monthly_temperature[selected_month_index])


# In[37]:


len(months) 
len(station_start_years)


# I learnt how to make list and update them
# I found the assert statements difficult to execute. Still facing issues. Would like some help.
# Change nothing

# In[ ]:




