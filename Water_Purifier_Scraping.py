#!/usr/bin/env python
# coding: utf-8

# In[17]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


# In[18]:


driver = webdriver.Chrome()


# In[19]:


def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup


# In[20]:


def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={'class':'_2kHMtA'}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link


# In[21]:


def get_product_name(soup):
    product_name= []
    try:
        name=soup.find('div',attrs={'class':'_4rR01T'}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name


# In[22]:


def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_30jeq3 _1_WHN1"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price


# In[23]:


def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class' : '_3LWZlK'}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings


# In[24]:


def get_specifications(soup):
    for item in soup.find_all("li", class_="_21Ahn-"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
            electricalandstorage= [spec[0].split(': ')[1] for spec in specifications]
            capacity = [spec[1] for spec in specifications]
            
            return ( electricalandstorage,capacity)


# In[25]:


url='https://www.flipkart.com/livpure-liv-bolt-copper-ro-uf-min-7-l-ro-uf-minerals-water-purifier/p/itmb8d6acc536844?pid=WAPG9FFKGAGFHWCZ&lid=LSTWAPG9FFKGAGFHWCZJEP3FZ&marketplace=FLIPKART&q=water+purifier&store=j9e%2Fabm%2Fi45&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&fm=organic&iid=en_iPmg%2BmfINJG7EmBYCJN%2FSrfhpndeuUvt%2FVhA%2BcQzSNN%2BoAOuEBgJUWgonP51thS1mpOWtshLK4VyKeSk2un5WA%3D%3D&ppt=clp&ppn=tvs-and-appliances-new-clp-store&ssid=xiqcp5tnbk0000001675857186480&qH=57f97975143685a0'


# In[26]:


data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : []})


# In[ ]:


data["Product_Url"] = product_links


# In[ ]:


df= pd.DataFrame()
def assign_to_dataframe(product_content):
    product_names = get_product_name(product_content)
    product_prices = get_product_price(product_content)
    product_ratings= get_product_ratings(product_content)
    df =pd.DataFrame({
           "Product Name": product_names,
            "Price": product_prices,
            "Ratings" : product_ratings
        })

    return df
for product in range(len(data)):
    product_url = data["Product_Url"].iloc[product]
    product_content = url_content(product_url)
    df1 = assign_to_dataframe(product_content)
    df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)
df


# In[ ]:




