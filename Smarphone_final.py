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

#Function to extract product_ratings of products 

def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class':"_3LWZlK"}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings

#Function to extract camera features of products 

def get_camera_features(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        camera_features = [spec[2] for spec in specifications]
    except:
        camera_features= "NO value available"
    return camera_features

#Function to extract battery details of products 

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

#Function to extract processor of products 

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

#Function to extract color of products 

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

#Function to extract display_size of products 

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
        if not display_size:
            display_size = "No value available"
    except:
         display_size = "No value available"
    return display_size

#Function to extract display_type of products 

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
        if not display_type:
            display_type = "No value available"
    except:
        display_type = "No value available"
    return display_type

#Function to extract resolution of products 

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
        if not resolution:
            resolution = "No value available"
    except:
        resolution = "No value available"
    return resolution

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

#Function to extract processor_type of products 

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
        if not processor_type:
            processor_type = "No value available"
    except:
         processor_type = "No value available"
    return processor_type

#Function to extract ram_size of products 

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
        if not ram_size:
            ram_size = "No value available"
    except:
        ram_size = "No value available"
    return ram_size

#Function to extract internal_storage of products 

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
        if not internal_storage:
            internal_storage = "No value available"
    except:
        internal_storage = "No value available"
    return internal_storage

#Creating dataframe for calculating the length of the dataframe containing the features

data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [],"camera_features":[],"battery_details":[],"Processor":[],"product_color":[],"model_name":[],"display_size":[],"display_type":[],"resolution":[],"operating_system":[],"processor_type":[],"ram_size":[],"internal_storage":[]})

#Scraping all the required features of each product

df=pd.DataFrame()
def assign_to_dataframe(product_content):
        product_names = get_product_name(product_content)
        product_prices = get_product_price(product_content)
        product_ratings= get_product_ratings(product_content)
        camera_featuress = get_camera_features(product_content)
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
                "camera_features":camera_featuress,
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

df.head(5)

# Converting the dataframe into a csv file

df.to_csv('smart_phone.csv', index=False)

#Converting the dataframe into a json file

df.to_json("smart_phone. json", orient='records')




