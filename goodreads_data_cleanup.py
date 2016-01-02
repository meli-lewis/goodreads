import re

import numpy as np
import pandas as pd



df = pd.read_csv("goodreads_library_export.csv")


# I don't care about most of these fields
df.drop(['Book Id', 'Author', 'Additional Authors', 'Original Publication Year',
         'Bookshelves with positions', 'My Review', 'Spoiler', 'Private Notes',
         'Read Count', 'Recommended For', 'Recommended By', 'Owned Copies',
         'Original Purchase Date', 'Original Purchase Location', 'Condition',
         'Condition Description', 'BCID'], axis=1, inplace=True)


# Goodreads outputs ISBNs as a formula in anticipation
# of being used with Excel. This converts it to a string.
df['ISBN'] = df['ISBN'].apply(lambda x: re.sub(r"[=|\"]", "", x))
df['ISBN13'] = df['ISBN13'].apply(lambda x: re.sub(r"[=|\"]", "", x))


# Format Date Added as pandas datetime,
# so it is easy to convert to other timestamp formats
df['Date Added'] = pd.to_datetime(df['Date Added'], format='%Y/%m/%d')
df['Date Read'] = pd.to_datetime(df['Date Read'], format='%Y/%m/%d')

# commented out because I dropped this column
""" df['Original Purchase Date'] = pd.to_datetime(df['Original Purchase Date'],
    format='%Y/%m/%d')"""


"""If you've yet to rate a book, its value is recorded by Goodreads as 0;
however, that's not strictly true! Here I use NumPy to convert a 0 rating
to something more akin to a missing value."""

df['My Rating'] = df['My Rating'].replace(0, np.nan)


def classifier(bookshelf):
    if "non-fiction" in str(bookshelf):
        return "non-fiction"
    elif "fiction" in str(bookshelf):
        return "fiction"
    else:
        return "undefined"


df['classification'] = df['Bookshelves'].apply(lambda x: classifier(x))

df.to_csv('full_table.csv')

# make a new dataframe with just the ISBN and Bookshelves data
df2 = df[['ISBN13', 'Bookshelves']]

"""
So, this looks like a pile of garbage because it's
transforming a field with a list of "bookshelves", aka
tags, into their own entries per field. I'm gonna be
a bad person for now and not document yet why I do this.
"""
df3 = df2['Bookshelves'].str.split(',').apply(pd.Series, 1).stack()
df3.index = df3.index.droplevel(-1)
df3.name = 'shelves'
df2.drop('Bookshelves', axis=1, inplace=True)
df4 = df2.join(df3)

# I make these two CSVs for easy use with Tableau. YMMV.
df4.to_csv('bookshelves.csv')
