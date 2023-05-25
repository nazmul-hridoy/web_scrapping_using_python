# pip3 install requests
import requests

# pip3 install beautifulsoup4
from bs4 import BeautifulSoup

# pip3 install pandas
import pandas as pd

books = []

for page_num in range(1,10):
  url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
  response = requests.get(url)
  response = response.content
  soup = BeautifulSoup(response, 'html.parser')
  ol = soup.find('ol')
  articles = ol.find_all('article', class_='product_pod')
  for values in articles:
    image = values.find('img')
    title = image.attrs['alt']
    starTag = values.find('p')
    star = starTag['class'][1]
    price = values.find('p', class_='price_color').text
    price = float(price[1:])
    books.append([title, star, price])
    

dataframe = pd.DataFrame(books, columns=['Title', 'Star Rating', 'Price'])
dataframe.to_csv('book_list.csv')




'''
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
Example
Create a simple Pandas DataFrame:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 


Result

     calories  duration
  0       420        50
  1       380        40
  2       390        45


'''