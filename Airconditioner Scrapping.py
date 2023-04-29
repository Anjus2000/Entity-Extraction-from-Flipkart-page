
#importing required libraries

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
    product_name = []
    try:
        name = soup.find('span', attrs={'class': "B_NuCI"}).text
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


#Function to extract capacity_in_tons of products 

def get_capacity_in_tons(soup):
    capacity_in_tons = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "capacity_in_tons":
                capacity_in_tons = cells[1].text.strip()
                break
        if not capacity_in_tons:
            capacity_in_tons = "No value available"
    except:
         capacity_in_tons = "No value available"
    return capacity_in_tons


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


#Function to extract product_type of products 

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


#Function to extract brand of products 

def get_brand(soup):
    brand = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "brand":
                brand = cells[1].text.strip()
                break
        if not brand:
            brand = "No value available"
    except:
        brand = "No value available"
    return brand


#Function to extract product_color  of products 

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


#Function to extract cooling_capacity of products 

def get_cooling_capacity(soup):
    cooling_capacity = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "cooling capacity":
                cooling_capacity = cells[1].text.strip()
                break
        if not cooling_capacity:
            cooling_capacity = "No value available"
    except:
        cooling_capacity = "No value available"
    return cooling_capacity


#Function to extract compressor of products 

def get_compressor(soup):
    compressor = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "compressor":
                compressor = cells[1].text.strip()
                break
        if not compressor:
            compressor = "No value available"
    except:
        compressor = "No value available"
    return compressor


#Function to extract remote_control availability of products 

def get_remote_control(soup):
    remote_control = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "remote control":
                remote_control = cells[1].text.strip()
                break
        if not remote_control:
            remote_control = "No value available"
    except:
        remote_control = "No value available"
    return remote_control


#Function to extract dust_filter of products 

def get_dust_filter(soup):
    dust_filter = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})[4]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "dust filter":
                dust_filter = cells[1].text.strip()
                continue
        if not dust_filter:
            dust_filter = "No value available"
    except:
        dust_filter = "No value available"
    return dust_filter


#Function to extract power_consumption of products 

def get_power_consumption(soup):
    power_consumption = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})[6]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "power consumption":
                power_consumption = cells[1].text.strip()
                continue
        if not power_consumption:
            power_consumption = "No value available"
    except:
        power_consumption = "No value available"
    return power_consumption


#Function to extract power_requirement of products 

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



# Define the URL
url_base = "https://www.flipkart.com/search?q=air%20conditioner&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

# Create an empty list to store data frames
df_list = []

# Scraping 
for page in range(1, 45):
    # Define the URL for each page
    url = url_base + str(page)
    
    # Get the content of the page
    url_contents = url_content(url)
    
    # Get the URLs for each product on the page
    product_links = get_product_url(url_contents)
    
    # Create an empty data frame
    data = pd.DataFrame(columns=[
        
        "Product_Url",
        "ProductName",
        "Price",
        "Ratings,"
        "Capacity, in tons"
        "ModelName,"
        "ProductType",
        "Brand",
        "ProductColor",
        "CoolingCapacity",
        "Compressor",
        "RemoteControl",
        "DustFilter",
        "PowerConsumption",
        "PowerRequirement"
       
    ])

    # Loop through each product on the page
    for product in range(len(product_links)):
        # Get the content of the product page
        product_url = product_links[product]
        product_content = url_content(product_url)

        # Get the product details and store them in a data frame
        product_names = get_product_name(product_content)
        product_prices = get_product_price(product_content)
        product_ratings= get_product_ratings(product_content)
        capacity_in_tons=get_capacity_in_tons(product_content)
        model_name = get_model_name(product_content)
        product_type = get_product_type(product_content)
        brand = get_brand(product_content)
        product_color= get_product_color(product_content)
        cooling_capacity= get_cooling_capacity(product_content)
        compressor= get_compressor(product_content)
        remote_control= get_remote_control(product_content)
        dust_filter= get_dust_filter(product_content)
        power_consumption= get_power_consumption(product_content)
        power_requirement= get_power_requirement(product_content)

        df = pd.DataFrame({
            "Product Name": product_names,
            "Price": product_prices,
            "Ratings" : product_ratings,
            "capacity_in_tons":capacity_in_tons,
            "model_name":model_name,
            "product_type":product_type,
            "brand":brand,
            "product_color":product_color,
            "cooling_capacity":cooling_capacity,
            "compressor":compressor,
            "remote_control":remote_control,
            "dust_filter":dust_filter,
            "power_consumption":power_consumption,
            "power_requirement":power_requirement,
            "Product_Url": product_url
            
        
            
        })
        

        data = pd.concat([data, pd.DataFrame.from_dict(df)], ignore_index=True)

    # Add the data frame to the list of data frames
    df_list.append(data)

# Concatenate all the data frames in the list into a single data frame
final_df = pd.concat(df_list, ignore_index=True)

# Export the data frame as a CSV file
final_df.to_csv("Airconditioner.csv", index=False)






