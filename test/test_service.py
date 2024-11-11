import pandas as pd
import requests

con = 'postgresql://radio:123456@151.248.122.251:5432/first'
data = pd.read_sql_table('flats', con)

dict_data = data.sample(2).to_dict(orient='records')

BASE = "http://151.248.122.251:5000/"
response = requests.post(BASE + "predict", json=dict_data)

print(response.json())
