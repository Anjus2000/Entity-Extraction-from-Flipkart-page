#Importing necessary libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome()

#Function to extract content from page

def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup
#Function for product url

def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={'class':'_4ddWXP'}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link

#Function for getting product name 

def get_product_name(soup):
    product_name= []
    try:
        name=soup.find('span',attrs={'class':"B_NuCI"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name

#Function for getting product price

def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_30jeq3 _16Jk6d"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price

#Function for getting ratings 

def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class' : '_3LWZlK'}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings

#function for language
def get_Language(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        supported_app = [spec[0].split(': ')[1] for spec in specifications]
    except:
       Language = "No rating available"
    return Language

#function for binding
def get_Binding(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        Binding= [spec[2] for spec in specifications]
    except:
        Binding = "NO value available"
    return Binding
#function for publisher
def get_Publisher(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        Publisher = [spec[3] for spec in specifications]
    except:
        Publisher= "NO value available"
    return Publisher

#function for genre
def get_genre(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        genre= [spec[4] for spec in specifications]
    except:
        genre= "NO value available"
    return genre

#function for ISBN
def get_isbn (soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        isbn = [spec[5] for spec in specifications]
    except:
        isbn= "NO value available"
    return isbn

#function for edtion
def get_edition(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        edition = [spec[6] for spec in specifications]
    except:
        edition= "NO value available"
    return edition

#Link of the product

url="https://www.flipkart.com/meditations/p/itmfbcm9fphnqzdp?pid=9789387585157&lid=LSTBOK9789387585157JS7VG1&marketplace=FLIPKART&q=books+to+read&store=bks&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&fm=organic&iid=c5a24269-2f35-40f0-b435-a94132a86e61.9789387585157.SEARCH&ppt=hp&ppn=homepage&ssid=mtcgs6cwkg0000001675849584049&qH=5e6d38a562c8230c"



data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : []}) 



df = pd.DataFrame()
def assign_to_dataframe(product_content):
    product_names = get_product_name(product_content)
    product_prices = get_product_price(product_content)
    product_ratings= get_product_ratings(product_content)
    df =pd.DataFrame({
           "Product Name": product_names,
            "Price": product_prices,
            "Ratings" : product_ratings'
            "Language":language,
            "Binding":binding,
            "Publisher":Publisher,
            "Genre":genre,
            "ISBN':isbn
            "Edition":edition
                                                                                           
        
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









