#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing required libraries


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


# In[4]:


# Function to extract content from page


# In[5]:


driver = webdriver.Edge()


# In[6]:


def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'lxml')
    return soup


# In[7]:


#Function to extract urls of products 


# In[8]:


def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={"_1fQZEK"}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link


# In[9]:


#Function to extract names of products 


# In[10]:


def get_product_name(soup):
    product_name= []
    try:
        name=soup.find('span',attrs={'class':"B_NuCI"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name



# In[11]:


#Function to extract price of products 


# In[12]:


def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_30jeq3 _16Jk6d"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price


# In[13]:


#Function to extract ratings of products 


# In[14]:


def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class':"_3LWZlK"}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings


# In[15]:


#Function to extract ram_size of products 


# In[16]:


def get_processor(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        processor = [spec[0] for spec in specifications]
    except:
        processor = "No rating available"
    return processor


# In[17]:


#Function to extract display of products 


# In[18]:


def get_ram_size(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        ram_size = [spec[1] for spec in specifications]
    except:
        ram_size = "NO value available"
    return ram_size


# In[19]:


#Function to extract camera details of products 


# In[20]:


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


# In[21]:


#Function to extract processor of products 


# In[22]:


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


# In[23]:


#Function to extract warranty of products 


# In[24]:


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


# In[25]:


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


# In[26]:


#website_link


# In[27]:


url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# In[28]:


#Creating dataframe for calculating the length of the dataframe containing the features


# In[29]:


data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [], "processor":[],"ram_size":[],"operating_system":[],"storage":[],"resolution":[],"warranty":[]})


# In[30]:


url_contents=url_content(url)


# In[31]:


#Getting Each product's link


# In[32]:


product_links=get_product_url(url_contents)







# In[33]:


#Assigning the each product's link to the variaable "Product_Url" in the dataframe


# In[34]:


data["Product_Url"] = product_links



# In[37]:


df = pd.DataFrame()
for page in range(1, 45):
    def assign_to_dataframe(product_content):
        product_names = get_product_name(product_content)
        product_prices = get_product_price(product_content)
        product_ratings= get_product_ratings(product_content)
        processors=get_processor(product_content)
        ram_sizes = get_ram_size(product_content)
        operating_systems = get_operating_system(product_content)
        storages = get_storage(product_content)
        resolutions= get_resolution(product_content)
        warranties= get_warranty(product_content)
        df =pd.DataFrame({
               "Product Name": product_names,
                "Price": product_prices,
                "Ratings" : product_ratings,
                "Processor":processors,
                "ram_size":ram_sizes,
                "Operating_System":operating_systems,
                 "Storage":storages,
                "Resolution":resolutions,
                "warranty":warranties
            })
        
        return df


# In[38]:


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

