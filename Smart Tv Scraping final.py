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
        operating_system = [spec[1].split(': ')[1] for spec in specifications]
    except:
        operating_system = "NO value available"
    return operating_system

##Function for resolutions

def get_resolutions(soup):
    resolution = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "hd technology & resolution":
                resolution = cells[1].text.strip()
                break
    except:
        resolution = "No value available"
    return resolution

#Function for sound outputs

def get_sound_outputs(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        sound_output = [spec[3].split(': ')[1] for spec in specifications]
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
        refresh_rate = [spec[4].split(': ')[1] for spec in specifications]
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
        if not color:
            color = "No value available"
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
        if not display_size:
            display_size = "No value available"
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
        if not screen_type:
            screen_type = "No value available"
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
        if not model_name:
            model_name = "No value available"
    except:
         model_name = "No value available"
    return model_name

#Function for storage memory

def get_storage_memory(soup):
    memory = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "storage memory":
                memory = cells[1].text.strip()
                continue
        if not memory:
            memory = "No value available"
    except:
         memory = "No value available"
    return memory

# Function for ram storage

def get_ram_storage(soup):
    ram = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "ram capacity":
                ram = cells[1].text.strip()
                continue
        if not ram:
            ram = "No value available"
    except:
         ram = "No value available"
    return ram

#Function for number of scores

def get_number_cores(soup):
    cores = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "number of cores":
                cores = cells[1].text.strip()
                break
        if not cores:
            cores = "No value available"
    except:
         cores = "No value available"
    return cores

#Function for getting processor 

def get_processor(soup):
    processor = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "processor":
                processor = cells[1].text.strip()
                continue
        if not processor:
            processor = "No value available"
    except:
         processor = "No value available"
    return processor

#Function for getting system language

def get_system_language(soup):
    language = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "system languages":
                language = cells[1].text.strip()
                continue
        if not language:
            language = "No value available"
            
    except:
         language = "No value available"
    return language

#Function for getting power requirements

def get_power_requirement(soup):
    power_requirement = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[6]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "power requirement":
                power_requirement = cells[1].text.strip()
                continue
        if not power_requirement:
             power_requirement = "No value available"
    except:
         power_requirement = "No value available"
    return power_requirement


#Creating dataframe for calculating the length of the dataframe containing the features

data = pd.DataFrame({"Product_Url" : [], "Product Name" : [], "Price" : [], "Ratings" : [],"Model Name" : [], "Supported Apps" : [],"Operating Systems" : [], 
                     "Display Size":[],"Screen Type":[], "Color":[],"Storage Memory" : [],"Ram Storage" : [],"Number of Cores":[],"Processor" :[],  "Resolutions" : [],
                     "System Language" : [],"Power Requirement" : [], "Refresh Rates":[], "Sound Output":[]})

#Scraping all the required features of each product

df=pd.DataFrame()
def assign_to_dataframe(product_content):
    product_names = get_product_name(product_content)
    product_prices = get_product_price(product_content)
    product_ratings= get_product_ratings(product_content)
    supported_appss = get_supported_apps(product_content)
    operating_systemss = get_operating_systems(product_content)
    resolutionss = get_resolutions(product_content)
    refresh_ratess = get_refresh_rates(product_content)
    product_color = get_product_color(product_content)
    product_display_size = get_display_size(product_content)
    product_screen_type = get_screen_type(product_content)
    product_model_name = get_model_name(product_content)
    product_storage_memory = get_storage_memory(product_content)
    product_ram_storage = get_ram_storage(product_content)
    product_numberof_cores = get_number_cores(product_content)
    product_processor = get_processor(product_content)
    system_language = get_system_language(product_content)
    product_power_requirement = get_power_requirement(product_content)
    product_sound_outputs = get_sound_outputs(product_content)
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
                    "Storage Memory" : product_storage_memory,
                    "Ram Storage" : product_ram_storage,
                    "Number of Cores" : product_numberof_cores,
                    "Processor" : product_processor,
                    "Resolutions" : resolutionss,
                    "System Language" : system_language,
                    "Power Requirement" : product_power_requirement,
                    "Refresh Rates" : refresh_ratess,
                    "Sound Output" : product_sound_outputs
                    
                    
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

df.to_csv('smart_tv.csv', index=False)

#Converting the dataframe into a json file

df.to_json("smart_tv. json", orient='records')
