#Importing necessary libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd


#Function to extract content from page

def url_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup

#Function for product url

def get_product_url(soup):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
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

#Function for product colour

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

#Function for display size 

def get_display_size(soup):
    display_size = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "display size":
                display_size = cells[1].text.strip()
                break
    except:
        display_size = "No value available"
    return display_size

#function for screen type

def get_screen_type(soup):
    screen_type = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "screen type":
                screen_type = cells[1].text.strip()
                break
    except:
         screen_type = "No value available"
    return screen_type


#Function for model name

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


#Creating dataframe for calculating the length of the dataframe containing the features

data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [],"Model Name" : [], "Supported Apps" : [],"Operating Systems" : [], "Display Size":[],"Screen Type":[], "Color":[], "Resolutions" : [], "Sound Outputs" : [], "Refresh Rates" : [],})


#Scraping all the required features of each product

df=pd.DataFrame()
def assign_to_dataframe(product_content):
    product_names = get_product_name(product_content)
    product_prices = get_product_price(product_content)
    product_ratings= get_product_ratings(product_content)
    supported_appss = get_specifications1(product_content)
    operating_systemss = get_specifications2(product_content)
    resolutionss = get_specifications3(product_content)
    sound_outputss = get_specifications4(product_content)
    refresh_ratess = get_specifications5(product_content)
    product_color = get_product_color(product_content)
    product_display_size = get_display_size(product_content)
    product_screen_type = get_screen_type(product_content)
    product_model_name = get_model_name(product_content)
    df = pd.DataFrame({
                   "Product Name": product_names,
                    "Price": product_prices,
                    "Ratings" : product_ratings,
                    "Model Name" : product_model_name,
                     "Supported Apps" : supported_appss,
                    "Operating Systems" : operating_systemss,
                    "Display Size" : product_display_size,
                    "Screen Type" : product_screen_type,
                    "Color" : product_color,
                    "Resolutions" : resolutionss,
                    "Sound Outputs" : sound_outputss,
                    "Refresh Rates" : refresh_ratess,
                    
                })

    return df


# Getting product deatails for 45 pages

for page in range(1, 46):
    url = f"https://www.flipkart.com/search?q=smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&as-pos=1&as-type=HISTORY&suggestionId=smart+tv%7CTelevisions&requestId=ac4665a8-c1ef-462b-9fb8-e5913908cc39"
    url_contents = url_content(url)
    product_link = get_product_url(url_contents)
    data["Product_Url"] = product_link
    
    for product in range(len(data)):
        product_url = data["Product_Url"].iloc[product]
        product_content = url_content(product_url)
        df1 = assign_to_dataframe(product_content)
        df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)

df.head()

#Converting the dataframe into a json file

smart_tv_json = df.to_json(orient='records')
