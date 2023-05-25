# process_of_scrapping_website
# through API
# HTML web scrapping using tool like bs4


# step-0 install requirements
# pip install requests
# pip install html5lib
# pip install bs4

import requests
from bs4 import BeautifulSoup

url = "https://www.bdtask.com"

# step-1 get the html
r = requests.get(url)  # r variable has all the HTML code
htmlContent = r.content  # r returns response so if we want the code we write r.content
# print(htmlContent) # printing the code
htmlText = r.text
# print(htmlText)

# step-2 parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())  #   print whole webpage in html format


# step-3 HTML TREE traversal

# get title of the webpage
title = soup.title
# print(title)   #   print title of the webpage
# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# # 4. Comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))


# Get all the paragraphs from the page
# paras = soup.find_all('p')
# print(paras)


# Get all the anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)
# for values in anchors:
# print(values.get('href'))

# Get first element in the HTML page
# print(soup.find('a') ) #find the first anchor tag in the page
# print(soup.find('p') ) #find the first paragraph tag in the page

# Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# Get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())


'''
#Get all the links from the page
all_links = set() #an empty set
for link_path in anchors:
     if (link_path.get('href') != '#'):
        link_paths = "htttps://codewithharry.com" + link_path.get('href')
        all_links.add(link_path)
        print(link_paths)
'''

navbarSupportedContent = soup.find(id='mega-dropdown-menu')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
'''
# print(navbarSupportedContent)
print(navbarSupportedContent.contents)

for elements in navbarSupportedContent.contents:
    print(elements)
 
'''

'''
for item in navbarSupportedContent.stripped_strings:
    print(item)
for item in navbarSupportedContent.strings:
    print(item)
'''
'''
# print(navbarSupportedContent.parent)   # direct_parent
for item in navbarSupportedContent.parents:
    # all_ancestors
    # print(item)
    print(item.name)
'''
# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)


# select class/id via . & #
elem = soup.select('.d-block')
print(elem)
