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

def get_supported_apps(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        supported_app = [spec[0].split(': ')[1] for spec in specifications]
    except:
        supported_app = "No rating available"
    return supported_app

#Function for operating systems

def get_operating_systems(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        operating_system = [spec[1] for spec in specifications]
    except:
        operating_system = "NO value available"
    return operating_system

##Function for resolutions

def get_resolutions(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        resolution = [spec[2] for spec in specifications]
    except:
        resolution = "NO value available"
    return resolution

#Function for sound outputs

def get_sound_outputs(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        sound_output = [spec[3] for spec in specifications]
    except:
        sound_output = "NO value available"
    return sound_output

#Function for refresh outputs

def get_refresh_rates(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        refresh_rate = [spec[4] for spec in specifications]
    except:
        refresh_rate = "NO value available"
    return refresh_rate


# Flipkart smart tv products link

url = "https://www.flipkart.com/search?q=smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&as-pos=1&as-type=HISTORY&suggestionId=smart+tv%7CTelevisions&requestId=ac4665a8-c1ef-462b-9fb8-e5913908cc39"

#Creating dataframe for calculating the length of the dataframe containing the features

data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [], "Supported Apps" : [],"Operating Systems" : [], "Resolutions" : [], "Refresh Rates" : [], "Refresh Rates" : []})

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
        supported_appss = get_supported_apps(product_content)
        operating_systemss = get_operating_systems(product_content)
        resolutionss = get_resolutions(product_content)
        sound_outputss = get_sound_outputs(product_content)
        refresh_ratess = get_refresh_rates(product_content)
        df =pd.DataFrame({
               "Product Name": product_names,
                "Price": product_prices,
                "Ratings" : product_ratings,
                 "Supported Apps" : supported_appss,
                "Operating Systems" : operating_systemss,
                "Resolutions" : resolutionss,
                "Sound Outputs" : sound_outputss,
                "Refresh Rates" : refresh_ratess
            })

        return df
    for product in range(len(data)):
        product_url = data["Product_Url"].iloc[product]
        product_content = url_content(product_url)
        df1 = assign_to_dataframe(product_content)
        df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)
df.head()

#Converting the dataframe into a json file

smart_tv_json = df.to_json(orient='records')
