
import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup

#get the url
url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=popularity"
response = requests.get(url)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, "html.parser")

print(soup.prettify)


products = []
prices = []
ratings = []
product = soup.find('div', attrs={'class': '_4rR01T'})
print(product)


#scraping
for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
    name = a.find('div', attrs={'class': '_4rR01T'})
    price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    rating = a.find('div', attrs={'class': '_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating)


#Data to dataframe
import pandas as pd
df = pd.DataFrame({'Product Name':products,'Prices':prices})
df.head()
