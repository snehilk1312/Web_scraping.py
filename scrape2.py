from bs4 import BeautifulSoup
import requests
import csv


source_code = requests.get("https://stallman.org/").text

soup = BeautifulSoup(source_code, 'lxml')

# print(soup.prettify())
divs = soup.find_all('div', class_="c2")

# print(divs)
# print(type(divs))
# for div in divs:    
#     print(div)
#     print('*'*15)
'''
for div in divs:
   download = div.find_all('a')
   for div in download:
       print(div)

'''
print("Apps suggested to not be used by Richard Stallman : ", '\n')

# saving the information in csv file
csv_file = open('stallman_scrape.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['App_Name'])

for a in soup.select('div.c2 a[href]'):
    App_Name = a['href'][1:-5]
    print(App_Name)
    csv_writer.writerow([App_Name])


csv_file.close()

