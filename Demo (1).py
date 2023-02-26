#!/usr/bin/env python
# coding: utf-8

# In[23]:


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
        name=soup.find('span',attrs={'class':"B_NuCI"}).text
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



#Function to extract ram_size of products 




#Function to extract display of products 







#Function to extract camera details of products 



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



#Function to extract processor of products 




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



#Function to extract warranty of products 



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


def get_product_color(soup):
    color = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "color":
                color = cells[1].text.strip()
                break
    except:
        color = "No value available"
    return color


def get_model_name(soup):
    model_name = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "model name":
                model_name = cells[1].text.strip()
                break
    except:
         model_name = "No value available"
    return model_name


def get_display_size(soup):
    display_size = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1] 
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "display size":
                display_size = cells[1].text.strip()
                break
    except:
         display_size = "No value available"
    return display_size


def get_display_type(soup):
    display_type = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1] 
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "display type":
                display_type = cells[1].text.strip()
                break
    except:
         display_type = "No value available"
    return display_type


def get_resolution(soup):
    resolution = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1] 
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "resolution":
                resolution = cells[1].text.strip()
                break
    except:
         resolution = "No value available"
    return resolution


def get_operating_system(soup):
    operating_system = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[2]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "operating system":
                operating_system = cells[1].text.strip()
                break
    except:
         operating_system = "No value available"
    return operating_system



def get_processor_type(soup):
    processor_type = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[2] 
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "processor type":
                processor_type = cells[1].text.strip()
                break
    except:
         processor_type = "No value available"
    return processor_type


def get_ram_size(soup):
    ram_size = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3] 
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "ram":
                ram_size = cells[1].text.strip()
                break
    except:
         ram_size = "No value available"
    return ram_size




def get_internal_storage(soup):
    internal_storage = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3] 
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "internal storage":
                internal_storage = cells[1].text.strip()
                break
    except:
         internal_storage = "No value available"
    return internal_storage





#website_link



url = "https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"



#Creating dataframe for calculating the length of the dataframe containing the features



data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [],"camera_details":[],"battery_details":[],"Processor":[],"product_color":[],"model_name":[],"display_size":[],"display_type":[],"resolution":[],"operating_system":[],"processor_type":[],"ram_size":[],"internal_storage":[]})



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
        camera_detailss = get_camera_details(product_content)
        battery_detailss = get_battery_details(product_content)
        processors= get_processor(product_content)
        product_colors=get_product_color(product_content)
        model_names=get_model_name(product_content)
        display_sizes=get_display_size(product_content)
        display_types=get_display_type(product_content)
        resolutions = get_resolution(product_content)
        operating_systems=get_operating_system(product_content)
        processor_types=get_processor_type(product_content)
        ram_sizes = get_ram_size(product_content)
        internal_storages=get_internal_storage(product_content)
        df =pd.DataFrame({
               "Product Name": product_names,
                "Price": product_prices,
                "Ratings" : product_ratings,
                "camera_details":camera_detailss,
                "battery_details":battery_detailss,
                "Processor":processors,
                "product_color":product_colors,
                "model_name":model_names,
                "display_size":display_sizes,
                "display_type":display_types,
                "resolution":resolutions,
                "operating_system":operating_systems,
                "processor_type":processor_types,
                "ram_size":ram_sizes,
                "internal_storage":internal_storages
                
            })
        
        return df





# In[24]:


for product in range(len(data)): 
       product_url = data["Product_Url"].iloc[product]
       product_content = url_content(product_url)
       df1 = assign_to_dataframe(product_content) 
       df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)
df.head(15)


# In[ ]:




