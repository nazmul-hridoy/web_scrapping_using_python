
from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://jobs.bdjobs.com/jobsearch.asp?fcatId=12&icatId="
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="row")

with open('bdjobs.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Company', 'Area', 'Experience']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
        company = list.find('div', class_="comp-name-text").text.replace('\n', '')
        area = list.find('div', class_="locon-text-d").text.replace('\n', '')
        experience = list.find('div', class_="exp-text-d").text.replace('\n', '')
        
        info = [title, company, area, experience]
        thewriter.writerow(info)
