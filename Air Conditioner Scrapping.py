#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing required libraries


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


# Function to extract content from page


driver = webdriver.Edge()


def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'lxml')
    return soup


#Function to extract urls of products 

def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={"_1fQZEK"}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link


#Function to extract names of products 


def get_product_name(soup):
    product_name= []
    try:
        name=soup.find('div',attrs={'class':"_4rR01T"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name



#Function to extract price of products 


def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_30jeq3 _16Jk6d"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price


#Function to extract ratings of products 


def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class':"_3LWZlK"}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings


#Function to extract capacity_in_tonsof products 


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



#Function to extract star_rating of products 


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


#Function to extract camera details of products 


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



#Function to extract storage of products 


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


#Function to extract resolution of products 


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



#website_link


url = "https://www.flipkart.com/search?q=air%20conditioner&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


#Creating dataframe for calculating the length of the dataframe containing the features



data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [], "capacity_in_tons":[],"star_rating":[],"operating_system":[],"storage":[],"resolution":[],"warranty":[]})


url_contents=url_content(url)



#Getting Each product's link



product_links=get_product_url(url_contents)



#Assigning the each product's link to the variaable "Product_Url" in the dataframe


data["Product_Url"] = product_links



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


for product in range(len(data)): 
       product_url = data["Product_Url"].iloc[product]
       product_content = url_content(product_url)
       df1 = assign_to_dataframe(product_content) 
       df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)
df.head(15)


#Converting the dataframe into a json file

Aircontioner_json = df.to_json(orient='records')

