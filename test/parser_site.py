import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

URL_base = "http://citystar.ru/detal.htm?d=43\
        &nm=%CE%E1%FA%FF%E2%EB%E5%ED\
        %E8%FF%20%20%CF%F0%EE%E4%E0%E\
        C%20%EA%E2%E0%F0%F2%E8%F0%F3%20%\
        E2%20%E3.%20%CC%E0%E3%ED%E8%F2%EE%E3%EE%F0%F1%EA%E5"

FILE_NAME = "data_flats.csv"
rows = []

for page in range(0, 10):
    URL = URL_base
    if page != 0:
        URL = URL_base + "&pN=" + str(page)

    r = requests.get(URL)
    print("Статус получения страницы №" + str(page) + ": ", r.status_code)
    r.encoding = 'cp1251'
    text = r.text

    soup1 = bs(text, "html.parser")
    apartments = soup1.find_all('tr', class_='tbb')

    #Как не странно, но сайт всегда отвечает кодом 200, даже если данные на запрашиваемой странице нет
    #Поэтому организуем проверку на наличие данных в ответе сервера
    if len(apartments) == 0:
    	break;
    	
    for aprt in apartments:
        fields = []
        for element in aprt.find_all('td'):
            fields.append(element.text)

        columns = [
            'photo',
            'date',
            'type_flat',
            'region',
            'address',
            'floor',
            'total_area',
            'living_area',
            'kitchen_area',
            'note',
            'price',
            'telephone',
            'agency',
            'email'
        ]

        rows.append(dict(zip(columns, fields)))

df = pd.DataFrame(rows)

#df = df.drop(['photo', 'address', 'note', 'telephone', 'agency', 'email'], axis=1)
print("Количество полученных квартир:", len(df))
df.to_csv(FILE_NAME)
con = 'postgresql://radio:123456@localhost/first'
df.to_sql(name='flats', con=con)


