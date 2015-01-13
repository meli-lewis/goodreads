
# coding: utf-8

# In[101]:

import bokeh.charts as bc
import matplotlib.pyplot as plt
import pandas as pd
import qgrid
import seaborn as sns
from IPython.display import Image

get_ipython().magic(u'matplotlib inline')
qgrid.nbinstall()


# In[102]:

#import data
t1 = pd.read_csv("goodreads_export.csv")


# In[103]:

#check your columns
t1.columns


# In[104]:

t1.info()


# In[105]:

t1['Bookshelves']


# In[106]:

'''check for whether your ISBNs were output as a formula, which I 
think Goodreads does in anticipation of import into Excel'''
a = t1.ix[0]['ISBN13']
print a


# In[107]:

# if the above begins with an equal sign, it is a formula
t1['ISBN13'] = t1['ISBN13'].str.replace('"', '')
t1['ISBN13'] = t1['ISBN13'].str.replace('=', '')
t1['ISBN'] = t1['ISBN'].str.replace('"', '')
t1['ISBN'] = t1['ISBN'].str.replace('=', '')


# In[108]:

t1


# In[109]:

t2.isnull().sum()


# In[110]:

'''See how dates are represented'''
b = t1.ix[0]['Date Added']
print b
type(b)


# In[111]:

# Format Date Added as pandas datetime, so it is easy to convert to other timestamp formats
t1['Date Added'] = pd.to_datetime(t1['Date Added'] , format = '%Y/%m/%d')
b = t1.ix[0]['Date Added']
print b
type(b)


# In[112]:

# Repeat for other date data
t1['Date Read'] = pd.to_datetime(t1['Date Read'] , format = '%Y/%m/%d')
t1['Original Purchase Date'] = pd.to_datetime(t1['Original Purchase Date'] , format = '%Y/%m/%d')


# In[113]:

t1.info()


# In[114]:

t1.to_csv('full_table.csv')


# In[115]:

# make a new dataframe with just the ISBN and Bookshelves data
t2 = t1[['ISBN13','Bookshelves']]


# In[116]:

t2


# In[117]:

t3 = t2['Bookshelves'].str.split(',').apply(pd.Series, 1).stack()
t3.index = t3.index.droplevel(-1)
t3.name = 'shelves'
t2.drop('Bookshelves', axis=1, inplace=True)
t4 = t2.join(t3)


# In[121]:

t4


# In[ ]:

t4.to_csv('bookshelves.csv')

