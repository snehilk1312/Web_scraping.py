from bs4 import BeautifulSoup
import requests


with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')     # passing file and parser


# print(soup.prettify())      # using prettify to properly represent with html indent

# title = soup.title.text            # for printing the 1st title tag in from our html file
# print(title)

# div = soup.find('div', class_="collapse navbar-collapse")    # we have used css class_ instead of css class coz python has class keyword
# print(div)

links = soup.find_all('a')          # returns a list
for link in links:
    print(link)
