
# coding: utf-8

import numpy as np
import pandas as pd


#import data
t1 = pd.read_csv("goodreads_export.csv")


#check your columns
t1.columns



t1['Bookshelves']



'''check for whether your ISBNs were output as a formula, which I 
think Goodreads does in anticipation of import into Excel'''
a = t1.ix[0]['ISBN13']
print a



# if the above begins with an equal sign, it is a formula
t1['ISBN13'] = t1['ISBN13'].str.replace('"', '')
t1['ISBN13'] = t1['ISBN13'].str.replace('=', '')
t1['ISBN'] = t1['ISBN'].str.replace('"', '')
t1['ISBN'] = t1['ISBN'].str.replace('=', '')



# make a new dataframe with just the ISBN and Bookshelves data
t2 = t1[['ISBN13','Bookshelves']]


# check for nulls
t2.isnull().sum()



'''Check the formatting of the date'''
b = t1.ix[0]['Date Added']
print b
type(b)

# Format Date Added as pandas datetime, so it is easy to convert to other timestamp formats
t1['Date Added'] = pd.to_datetime(t1['Date Added'] , format = '%Y/%m/%d')
b = t1.ix[0]['Date Added']
print b
type(b)

# Repeat for other date data
t1['Date Read'] = pd.to_datetime(t1['Date Read'] , format = '%Y/%m/%d')
t1['Original Purchase Date'] = pd.to_datetime(t1['Original Purchase Date'] , format = '%Y/%m/%d')

t1




t1.to_csv('full_table.csv')


t2.to_csv('bookshelves.csv')

