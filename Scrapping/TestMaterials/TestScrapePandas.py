import pandas as pd
import requests
from bs4 import BeautifulSoup

'''
year = '20'
no = 'huh'
str = "yes no {} what {}"
up = str.format(year, no)
print(up)
'''


url = 'https://en.wikipedia.org/wiki/List_of_national_capitals'
tables = pd.read_html(url)
print(len(tables),'\n')
df = tables[1]
df.to_csv('capitals.csv')
print(df.head())


url = 'https://quotes.toscrape.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    for item in soup.find_all('span', class_='text'):
            data.append(item.text.strip())
    df = pd.DataFrame(data, columns=['Column_Name'])
    df.to_csv('quotes.csv')
    print(df)
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)