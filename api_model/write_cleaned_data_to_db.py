import pandas as pd

data = pd.read_csv('cleaned_data.csv', index_col=0)
print(data.head())
con = 'postgresql://radio:123456@db/first'
data.to_sql(name='flats', con=con)
