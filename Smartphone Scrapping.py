#Importing required libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# Function to extract content from page

def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup

driver = webdriver.Edge()


#Function to extract urls of products

def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={"_3liAhj"}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link


#Function to extract names of products 

def get_product_name(soup):
    product_name= []
    try:
        name=soup.find('span',attrs={'class':"_2cLu-l"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name


#Function to extract price of products

def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_30jeq3 _1_WHN1"}).text
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

def get_ram_size(soup):
    specifications=[]
    for item in soup.find_all("div", class_="fMghEO"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="rgWa7D")]
            specifications.append(item_specifications)
    try:
        ram_size = [spec[0].split(': ')[1] for spec in specifications]
    except:
        ram_size = "No rating available"
    return ram_size

#Function to extract display of products 

def get_resolution(soup):
    specifications=[]
    for item in soup.find_all("div", class_="fMghEO"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="rgWa7D")]
            specifications.append(item_specifications)
    try:
        resolution = [spec[1] for spec in specifications]
    except:
        resolution = "NO value available"
    return resolution

#Function to extract camera details of products 

def get_camera_details(soup):
    specifications=[]
    for item in soup.find_all("div", class_="fMghEO"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="rgWa7D")]
            specifications.append(item_specifications)
    try:
        camera_details = [spec[2] for spec in specifications]
    except:
        camera_details= "NO value available"
    return camera_details

#Function to extract processor of products 

def get_processor(soup):
    specifications=[]
    for item in soup.find_all("div", class_="fMghEO"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="rgWa7D")]
            specifications.append(item_specifications)
    try:
        processor= [spec[3] for spec in specifications]
    except:
        processor = "NO value available"
    return processor

#Function to extract warranty of products 

def get_warranty(soup):
    specifications=[]
    for item in soup.find_all("div", class_="fMghEO"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="rgWa7D")]
            specifications.append(item_specifications)
    try:
        warranty = [spec[3] for spec in specifications]
    except:
        warranty = "NO value available"
    return warranty

#website_link

url = "https://www.flipkart.com/search?q=smart%20pjone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


#Creating dataframe for calculating the length of the dataframe containing the features


data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [], "ram_size":[],"resolution":[],"camera":[],"processor":[],"warranty":[]})


url_contents=url_content(url)


#Getting Each product's link

product_links=get_product_url(url_contents)


#Assigning the each product's link to the variaable "Product_Url" in the dataframe


data["Product_Url"] = product_links

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
                "ram_size":ram_size,
                "resolution":resolution,
                "camera_details":camera_details,
                "processor":processor,
                "warranty":warranty
            })
        
        return df

for product in range(len(data)):
       product_url = data["Product_Url"].iloc[product]
       product_content = url_content(product_url)
       df1 = assign_to_dataframe(product_content) 
       df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)
df.head()

#Converting the dataframe into a json file

smart_phone_json = df.to_json(orient='records')






