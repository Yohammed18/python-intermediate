# Pandas is a powerful Python library for data manipulation and analysis. It provides data structures like dataframes, which are similar to tables in a database or spreadsheets, and a wide range of functions for data cleaning, transformation, and exploration. Pandas is widely used in data science and data analysis projects, especially for working with smaller to medium-sized datasets that fit into memory.
import pandas as pd 

# read the csv file and stores in a variable which we'll use to manipulate
# You have two option when you want to stare the file. Downloading the csv file directly in the same directory with your work python file or get the url where the csv raw data is hosted.
pokemons = pd.read_csv('https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv')

# print out the type of object the file is... (is should be of type DataFrame since that is what )
print(type(pokemons))

# Jupyter (formerly IPython) Notebooks: Jupyter Notebooks are interactive computing environments that allow users to create and share documents containing live code, visualizations, explanatory text, and equations. They support multiple programming languages, including Python, R, and Julia, but are most commonly associated with Python. Jupyter Notebooks are widely used in data science and scientific computing for tasks like data exploration, analysis, visualization, and documentation.
# to run jupyter notebook on the cmd (fter you installed jupyter localy via anaconda or conda) line insert python notebook.

# print the first 5 records on the pokemon table
print(pokemons.head(5))
print('\n')
# In Pandas, a table is of type DataFrame, whereas a column is of type Series
# get all the records under the series 'Name'
name_series = pokemons['Attack']
print(name_series.max())
print('\n')
print(pokemons.describe())


# REMEMBER
# Import the package, aka import pandas as pd. A table of data is stored as a pandas DataFrame. Each column in a DataFrame is a Series. You can do things by applying a method to a DataFrame or Series

print('\n')
# to see the datatype for each series use the variable dtypes
print(pokemons.dtypes)
print('\n')
# print technial summary of the pokemon dataframe
print(pokemons.info())

