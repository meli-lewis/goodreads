
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



#make a new dataframe with just the ISBN and Bookshelves data
t2 = t1[['ISBN13','Bookshelves']]



t1


# check for nulls
t4.isnull().sum()


t1.to_csv('full_table.csv')



t4.to_csv('bookshelves.csv')

