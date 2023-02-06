import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

driver = webdriver.Edge()

def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup



def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    for item in soup.find_all('a',href=True, attrs={'class':'_1fQZEK'}):
        rest_link = item['href']
        product_link.append(rest_link)
    return product_link



def get_product_name(soup):
    product_name= []
    try:
        name=soup.find('span',attrs={'class':"B_NuCI"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name



def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_30jeq3 _16Jk6d"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price



def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class' : '_3LWZlK'}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings



url = "https://www.flipkart.com/search?q=smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&as-pos=1&as-type=HISTORY&suggestionId=smart+tv%7CTelevisions&requestId=ac4665a8-c1ef-462b-9fb8-e5913908cc39"
driver.get(url)

url_content=get_product_url(driver)


get_product_url(url_content)


data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : []})

for product in range(len(data)):
    product_url = data['Product_Url'].iloc[product]
    product_content = url_content(product_url)

    get_product_name(product_content)
    get_product_price(product_content)
    get_product_ratings(product_content)
    # get_specifications(product_content)
