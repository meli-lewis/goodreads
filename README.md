Goodreads Transformation
=========

To use this notebook you must have Python 3 and Jupyter Notebook on your system. If you already use the IPython Notebook, updating should be easy.

If this ever gets more complicated I'll upload a Requirements file, but for now:

```bash
$ pip3 install jupyter
$ pip3 install pandas
```

The purpose of this notebook is both to make the CSV one exports from Goodreads more amenable to analysis. I've only addressed the two most obvious issues so far, and invite anyone interested to help me make this even better!

1. ISBNs written as formulae

My hunch is that this is a workaround Goodreads implemented because ISBNs are typically composed exclusively of integers and will be interpreted as numbers by software like Excel, which changes the representation of that number for the user (by doing things like dropping leading 0s). I think because it's not possible with a CSV to specify the data type of the column (ideally as a string here, so the exact number is reproduced), Goodreads made the cell value itself a formula describing the ISBN as a string. This is fine for Excel, but not for Python, so I wrote what is probably inefficient code for dropping the punctuation that makes that possible.

2. Bookshelf column composed of greater than one value

Let me know what might be a more elegant solution, but I made a second table to pull the bookshelf tags from the first so each tag might have its own row, with ISBN13 as its key. A couple of values in my dataset may be null because an ISBN13 value was not included, which I think is just a data problem on Goodreads' side, but perhaps you won't have that issue.

3. Formatted full dates to Pandas datetime objects

Not sure if this is everyone's favorite format, but this would be helpful for studying patterns over time. Changed the format on Date Added, Date Read, and Original Purchase Date.
