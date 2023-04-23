
#importing required libraries

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


#Function to extract model_name of products

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
        if not model_name:
            model_name = "No value available"
    except:
         model_name = "No value available"
    return model_name




#Function to extract product_color of products 


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
        if not color:
            color = "No value available"
    except:
        color = "No value available"
    return color

#Function to extract camera model_name of products 


#Function to extract battery_backup of products 


def get_battery_backup(soup):
    battery_backup = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "battery backup":
                battery_backup = cells[1].text.strip()
                break
        if not battery_backup:
            battery_backup = "No value available"
    except:
        battery_backup = "No value available"
    return battery_backup


#Function to extract type of products 


def get_product_type(soup):
    product_type = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "type":
                product_type = cells[1].text.strip()
                break
        if not product_type:
            product_type = "No value available"
    except:
        product_type = "No value available"
    return product_type


#Function to extract processor_names of products 


def get_processor_name(soup):
    processor_name = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "processor name":
                processor_name = cells[1].text.strip()
                break
        if not processor_name:
            processor_name = "No value available"
    except:
        processor_name = "No value available"
    return processor_name

#Function to extract processor_brand of products 


def get_processor_brand(soup):
    processor_brand = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "processor brand":
                processor_brand = cells[1].text.strip()
                break
        if not processor_brand:
            processor_brand = "No value available"
    except:
        processor_brand = "No value available"
    return processor_brand

#Function to extract ssd_capacity of products 


def get_ssd_capacity(soup):
    ssd_capacity = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "ssd capacity":
                ssd_capacity = cells[1].text.strip()
                break
        if not ssd_capacity:
            ssd_capacity = "No value available"
    except:
        ssd_capacity = "No value available"
    return ssd_capacity

#Function to extract ram_size of products 

def get_ram_size(soup):
    ram_size = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1] 
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "ram":
                ram_size = cells[1].text.strip()
                break
        if not ram_size:
            ram_size = "No value available"
    except:
        ram_size = "No value available"
    return ram_size


#Function to extract ram_type of products 


def get_ram_type(soup):
    ram_type = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "ram type":
                ram_type = cells[1].text.strip()
                break
        if not ram_type:
            ram_type = "No value available"
    except:
        ram_type = "No value available"
    return ram_type

#Function to extract graphic_processor of products 


def get_graphic_processor(soup):
    graphic_processor = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "graphic processor":
                graphic_processor = cells[1].text.strip()
                break
        if not graphic_processor:
            graphic_processor = "No value available"
    except:
        graphic_processor = "No value available"
    return graphic_processor

#Function to extract operating_system of products 



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
        if not operating_system:
            operating_system = "No value available"
    except:
        operating_system = "No value available"
    return operating_system

#Function to extract screen_resolution of products 


def get_screen_resolution(soup):
    screen_resolution = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "screen resolution":
                screen_resolution = cells[1].text.strip()
                break
        if not screen_resolution:
            screen_resolution = "No value available"
    except:
        screen_resolution = "No value available"
    return screen_resolution

#Function to extract screen_size of products 


def get_screen_size(soup):
    screen_size = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "screen size":
                screen_size = cells[1].text.strip()
                break
        if not screen_size:
            screen_size = "No value available"
    except:
        screen_size = "No value available"
    return screen_size


#website_link


url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


#Creating dataframe for calculating the length of the dataframe containing the features


data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [], "model_name":[],"product_color":[],"product_type":[],"":[],"processor_name":[],"processor_brand":[],"ssd_capacity":[],"ram_size":[],"ram_type":[],"graphic_processor":[],"operating_system":[],"screen_resolution":[],"screen_size":[]})


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
        model_name =get_model_name(product_content)
        product_color = get_product_color(product_content)
        product_type = get_product_type(product_content)
        processor_name = get_processor_name(product_content)
        processor_brand= get_processor_brand(product_content)
        ssd_capacity= get_ssd_capacity(product_content)
        ram_size= get_ram_size(product_content)
        ram_type= get_ram_type(product_content)
        graphic_processor= get_graphic_processor(product_content)
        operating_system= get_operating_system(product_content)
        screen_resolution= get_screen_resolution(product_content)
        screen_size= get_screen_size(product_content)


        df =pd.DataFrame({
               "Product Name": product_names,
                "Price": product_prices,
                "Ratings" : product_ratings,
                "model_name":model_name,
                "product_color":product_color,
                "product_type":product_type,
                "processor_name":processor_name,
                "processor_brand":processor_brand,
                "ssd_capacity":ssd_capacity,
                "ram_size":ram_size,
                "ram_type":ram_type,
                "graphic_processor":graphic_processor,
                "Operating_System":operating_system,
                "screen_resolution":screen_resolution,
                "screen_size":screen_size
            })
        
        return df





for product in range(len(data)): 
       product_url = data["Product_Url"].iloc[product]
       product_content = url_content(product_url)
       df1 = assign_to_dataframe(product_content) 
       df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)
df.head(15)









