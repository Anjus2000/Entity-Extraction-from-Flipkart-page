#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing required libraries


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


# In[3]:


# Function to extract content from page


# In[4]:


driver = webdriver.Edge()


# In[5]:


def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'lxml')
    return soup


# In[6]:


#Function to extract urls of products 


# In[7]:


def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={"_1fQZEK"}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link


# In[8]:


#Function to extract names of products 


# In[9]:


def get_product_name(soup):
    product_name= []
    try:
        name=soup.find('div',attrs={'class':"_4rR01T"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name



# In[10]:


#Function to extract price of products 


# In[11]:


def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_30jeq3 _16Jk6d"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price


# In[12]:


#Function to extract ratings of products 


# In[13]:


def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class':"_3LWZlK"}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings


# In[14]:


#Function to extract capacity_in_tonsof products 


# In[15]:


def get_capacity_in_tons(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        capacity_in_tons = [spec[0] for spec in specifications]
    except:
        capacity_in_tons = "No rating available"
    return capacity_in_tons


# In[16]:


#Function to extract star_rating of products 


# In[17]:


def get_star_rating(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        star_rating = [spec[1] for spec in specifications]
    except:
        star_rating= "NO value available"
    return star_rating


# In[18]:


#Function to extract camera details of products 


# In[52]:


def get_operating_system(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        operating_system = [spec[2] for spec in specifications]
    except:
        operating_system= "NO value available"
    return operating_system


# In[20]:


#Function to extract storage of products 


# In[21]:


def get_storage(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        storage= [spec[3] for spec in specifications]
    except:
        storage = "NO value available"
    return storage


# In[22]:


#Function to extract resolution of products 


# In[23]:


def get_resolution(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        resolution = [spec[4] for spec in specifications]
    except:
        resolution = "NO value available"
    return resolution


# In[24]:


def get_warranty(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        warranty = [spec[5] for spec in specifications]
    except:
        warranty = "NO value available"
    return warranty


# In[25]:


#website_link


# In[26]:


url = "https://www.flipkart.com/search?q=air%20conditioner&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# In[27]:


#Creating dataframe for calculating the length of the dataframe containing the features


# In[53]:


data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [], "capacity_in_tons":[],"star_rating":[],"operating_system":[],"storage":[],"resolution":[],"warranty":[]})


# In[54]:


url_contents=url_content(url)


# In[55]:


#Getting Each product's link


# In[56]:


product_links=get_product_url(url_contents)







# In[57]:


#Assigning the each product's link to the variaable "Product_Url" in the dataframe


# In[58]:


data["Product_Url"] = product_links



# In[63]:


df = pd.DataFrame()
for page in range(1, 45):
    def assign_to_dataframe(product_content):
        product_names = get_product_name(product_content)
        product_prices = get_product_price(product_content)
        product_ratings= get_product_ratings(product_content)
        capacity_in_tons=get_capacity_in_tons(product_content)
        star_ratings = get_star_rating(product_content)
        operating_systems = get_operating_system(product_content)
        storages = get_storage(product_content)
        resolutions= get_resolution(product_content)
        warranties= get_warranty(product_content)
        df =pd.DataFrame({
               "Product Name": product_names,
                "Price": product_prices,
                "Ratings" : product_ratings,
                "capacity_in_tons":capacity_in_tons,
                "star_rating":star_ratings,
                "Operating_System":operating_systems,
                 "Storage":storages,
                "Resolution":resolutions,
                "warranty":warranties
            })
        
        return df


# In[64]:


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

