# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:55:08 2019

@author: risoms
"""
import numpy as np
import pandas as pd
import pathlib as Path


#%% constants
path = '../data/variants.xlsx'

#%%
# import data
## keep Null values added directly to table. any empty cells will be converted to np.null
df = pd.read_csv('../data/variants.tsv', delimiter='\t', encoding='utf-8', parse_dates=['Last Evaluated','Last Updated'], keep_default_na=False, na_values='')

# create index column
df['id'] = df.index

# remove whitespace column names
df.columns = df.columns.str.replace(' ', '_')

# identify columns and types
_columns = list(df.columns)
_types = [str(x.type) for x in df.dtypes.to_list()]
summary = pd.DataFrame({'columns': _columns,'types':_types})
## sample
sample = df.head(100)

# set columns as categorical based on variable diversity
## explore gene unique as example
geneUnique = df['Gene'].value_counts()
summary['unique'] = summary['columns'].map(df.nunique())
summary['missing'] = summary['columns'].map(len(df.index)-df.count())

## make columns with small number of unique values into categorical
unique = summary.loc[(summary['unique'] <= 5000) & (summary['missing'] <= 20000)].reset_index(drop=True)

## change dtype
### categories
_uniqueList = unique['columns'].to_list()
df[_uniqueList] = df[_uniqueList].apply(lambda x: x.astype('category'))
_dateList = ['Last_Evaluated','Last_Updated'];
df[_dateList] = df[_dateList].apply(lambda x: x.astype('datetime64[ns]'))

#%% export test data
# export to json (for website debugging)
debug = df.head(100)
debug.to_json('../data/test.json', orient="records")

# export to sqlite database
import sqlite3
engine = sqlite3.connect('../data/test.sqlite3')
debug.to_sql(name='variants', con=engine, if_exists='replace', index=True, chunksize=10000)
engine.close()
#%% export real data
# export to json (for website debugging)
df.to_json('../data/invitae.json', orient="records")

# export to sqlite database
import sqlite3
engine = sqlite3.connect('../data/invitae.sqlite3')
df.to_sql(name='variants', con=engine, if_exists='replace', index=True, chunksize=10000)
engine.close()

































