#Importing necessary libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

driver = webdriver.Edge()

#Function to extract content from page

def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'lxml')
    return soup

#Function for product url

def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={'class':'_1fQZEK'}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link

#Function for product name

def get_product_name(soup):
    product_name = []
    try:
        name = soup.find('span', attrs={'class': "B_NuCI"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    # product_name = "Product Name"
    return product_name

#Function for product prices

def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div', attrs={'class': "_30jeq3 _16Jk6d"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price

#Function for product ratings

def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs={'class': '_3LWZlK'}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings

#Function for supported apps

def get_iphone_rom(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        iphone_rom = [spec[0].split(': ')[1] for spec in specifications]
    except:
        iphone_rom = "No rating available"
    return iphone_rom

#Function for operating systems

def get_iphone_display(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        iphone_display = [spec[1] for spec in specifications]
    except:
        iphone_display = "NO value available"
    return iphone_display

##Function for resolutions

def get_iphone_frontcamera(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        iphone_frontcamera = [spec[2] for spec in specifications]
    except:
        iphone_frontcamera = "NO value available"
    return iphone_frontcamera

#Function for sound outputs

def get_iphone_processor(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        processor = [spec[3] for spec in specifications]
    except:
        processor = "NO value available"
    return processor

# Flipkart iphone products link

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

#Creating dataframe for calculating the length of the dataframe containing the features

data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [], "supported_apps" : [],"operating_systems" : [], "resolutions" : [], "sound_outputs" : [], "refresh_rates" : []})

url_contents=url_content(url)

#Getting Each product's link

product_link = get_product_url(url_contents)

#Assigning the each product's link to the variaable "Product_Url" in the dataframe

data["Product_Url"] = product_link

#Scraping all the required features of each product

df = pd.DataFrame()
for page in range(1, 45):
    def assign_to_dataframe(product_content):
        product_names = get_product_name(product_content)
        product_prices = get_product_price(product_content)
        product_ratings= get_product_ratings(product_content)
        iphone_roms = get_iphone_rom(product_content)
        iphone_displays = get_iphone_display(product_content)
        iphone_froncameras = get_iphone_frontcamera(product_content)
        iphone_processors = get_iphone_processor(product_content)

        df =pd.DataFrame({
               "Product Name": product_names,
                "Price": product_prices,
                "Ratings" : product_ratings,
                 "Rom" : iphone_roms,
                "Display" : iphone_displays,
                "Front Camera" : iphone_froncameras,
                "Processor" : iphone_processors

            })

        return df
    for product in range(len(data)):
        product_url = data["Product_Url"].iloc[product]
        product_content = url_content(product_url)
        df1 = assign_to_dataframe(product_content)
        df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)
df.head()

#Converting the dataframe into a json file

iphone_json = df.to_json(orient='records')
