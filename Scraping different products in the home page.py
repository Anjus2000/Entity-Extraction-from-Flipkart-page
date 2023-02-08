from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Intializing driver
driver = webdriver.Edge()

products=[] #List to store name of the product
prices=[] #List to store price of the product

driver.get('https://www.flipkart.com/')

content = driver.page_source
soup = BeautifulSoup(content)


for a in soup.findAll('a',href=True, attrs={'class':'_6WQwDJ T88g6k'}):
    name=a.find('div', attrs={'class':'_3LU4EM'})
    price=a.find('div', attrs={'class':'_2tDhp2'})
    products.append(name.text)
    prices.append(price.text)

df= pd.DataFrame({'Product':products, 'Price':prices})
df.head()
