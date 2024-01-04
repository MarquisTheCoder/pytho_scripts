
# Import libraries
import urllib
import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import matplotlib.pyplot as plt
from io import BytesIO 

# Beautiful soup function
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,} 

def make_soup(url):
    request= urllib.request.Request(url, None,headers) 
    thepage = urllib.request.urlopen(request)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

# Get total number of pages 

site = 'https://www.asos.com/us/women/dresses/cat/?cid=8799'
soup = make_soup(site)
element = soup.find('p', class_='label_Ph1fi')
element = element.text

numbers = re.findall(r'\d{1,3}(?:,\d{3})*', element)

if len(numbers) >= 2:
    offset = int(numbers[0].replace(',', ''))
    num_images = int(numbers[1].replace(',', ''))
    num_pages = int(num_images / offset)
    print(f"Images Per Page: {offset}")
    print(f"Total Images: {num_images}")
    print(f"Total Pages:{num_pages}")
else:
    print("Numbers not found")

product_urls = []
for i in range(5): # testing with 5 instead of num_pages
    site = f'https://www.asos.com/us/women/dresses/cat/?cid=8799&page={i}'
    soup = make_soup(site)

    url_cnt = 0
    for product in soup.select('a[class*="productLink"]'):
        href = product.get('href')
        if href:
            product_urls.append(href)
            url_cnt += 1
    print(f'Page {i} done. URLs collected: {url_cnt}')

print(f'Total number of product urls: {len(product_urls)}')