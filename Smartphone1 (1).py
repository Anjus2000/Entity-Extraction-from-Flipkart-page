#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing required libraries


# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


# In[ ]:


# Function to extract content from page


# In[ ]:


driver = webdriver.Edge()


# In[ ]:


def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'lxml')
    return soup


# In[ ]:


#Function to extract urls of products 


# In[ ]:


def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={"_1fQZEK"}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link


# In[ ]:


#Function to extract names of products 


# In[ ]:


def get_product_name(soup):
    product_name= []
    try:
        name=soup.find('span',attrs={'class':"B_NuCI"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name



# In[ ]:


#Function to extract price of products 


# In[ ]:


def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_30jeq3 _16Jk6d"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price


# In[ ]:


#Function to extract ratings of products 


# In[ ]:


def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class':"_3LWZlK"}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings


# In[ ]:


#Function to extract ram_size of products 


# In[ ]:


def get_ram_size(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        ram_size = [spec[0] for spec in specifications]
    except:
        ram_size = "No rating available"
    return ram_size


# In[ ]:


#Function to extract display of products 


# In[ ]:


def get_resolution(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        resolution = [spec[1] for spec in specifications]
    except:
        resolution = "NO value available"
    return resolution


# In[ ]:


#Function to extract camera details of products 


# In[ ]:


def get_camera_details(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        camera_details = [spec[2] for spec in specifications]
    except:
        camera_details= "NO value available"
    return camera_details


# In[ ]:


#Function to extract processor of products 


# In[ ]:


def get_battery_details(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        battery_details= [spec[3] for spec in specifications]
    except:
        battery_details = "NO value available"
    return battery_details


# In[ ]:


#Function to extract warranty of products 


# In[ ]:


def get_processor(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        processor = [spec[4] for spec in specifications]
    except:
        processor = "NO value available"
    return processor


# In[ ]:


#website_link


# In[ ]:


url = "https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# In[ ]:


#Creating dataframe for calculating the length of the dataframe containing the features


# In[ ]:


data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [], "ram_size":[],"resolution":[],"camera_details":[],"battery_details":[],"Processor":[]})


# In[ ]:


url_contents=url_content(url)


# In[ ]:


#Getting Each product's link


# In[ ]:


product_links=get_product_url(url_contents)







# In[ ]:


#Assigning the each product's link to the variaable "Product_Url" in the dataframe


# In[ ]:


data["Product_Url"] = product_links



# In[ ]:


df = pd.DataFrame()
for page in range(1, 45):
    def assign_to_dataframe(product_content):
        product_names = get_product_name(product_content)
        product_prices = get_product_price(product_content)
        product_ratings= get_product_ratings(product_content)
        ram_sizes = get_ram_size(product_content)
        resolutions = get_resolution(product_content)
        camera_detailss = get_camera_details(product_content)
        battery_detailss = get_battery_details(product_content)
        processors= get_processor(product_content)
        df =pd.DataFrame({
               "Product Name": product_names,
                "Price": product_prices,
                "Ratings" : product_ratings,
                "ram_size":ram_sizes,
                "resolution":resolutions,
                "camera_details":camera_detailss,
                "battery_details":battery_detailss,
                "Processor":processors
            })
        
        return df


# In[ ]:


for product in range(len(data)): 
       product_url = data["Product_Url"].iloc[product]
       product_content = url_content(product_url)
       df1 = assign_to_dataframe(product_content) 
       df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)
df.head(15)


# In[ ]:


#Converting the dataframe into a json file



# In[ ]:


smart_phone_json = df.to_json(orient='records')

