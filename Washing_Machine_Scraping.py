#!/usr/bin/env python
# coding: utf-8

# In[60]:


get_ipython().system('pip install selenium')


# In[61]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


# In[62]:


driver = webdriver.Chrome()


# In[63]:


def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup


# In[64]:


def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={'class':'_1kLt05'}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link


# In[65]:


def get_product_name(soup):
    product_name= []
    try:
        name=soup.find('span',attrs={'class':"B_NuCI"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name


# In[66]:


def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_25b18c"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price


# In[67]:


def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class' : '_3LWZlK'}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings


# In[68]:


def get_specifications(soup):
    for item in soup.find_all("li", class_="_21Ahn-"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
            load = [spec[0].split(': ')[1] for spec in specifications]
            rpm = [spec[1] for spec in specifications]
            washes = [spec[2] for spec in specifications]
            rating = [spec[3] for spec in specifications]
            weight = [spec[4] for spec in specifications]
           
            return ( load,rpm,washes,rating,weight)


# In[69]:


url = 'https://www.flipkart.com/whirlpool-7-kg-magic-clean-5-star-semi-automatic-top-load-black-grey/p/itmee28cf6539c3f?pid=WMNGF9W8K8R9V8DA&marketplace=FLIPKART'
driver.get(url)


# In[70]:


data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : []})


# In[71]:


url_contents=url_content(url)


# In[72]:


product_links=get_product_url(url_contents)


# In[73]:


data["Product_Url"] = product_links


# In[77]:


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


# In[78]:


data


# In[79]:


df


# In[ ]:





# In[ ]:




