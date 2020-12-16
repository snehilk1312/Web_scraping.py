import requests
from bs4 import BeautifulSoup
import urllib.request


url = "https://www.reddit.com/r/trippinthroughtime/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

images = soup.find_all("img", attrs={"alt": "Post image"})

number = 0

for image in images:
    image_src = image['src']
    print(image_src)
    urllib.request.urlretrieve(image_src, f'{number}.jpg')
    number += 1


