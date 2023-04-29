#import required libraries

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





# Define the URL
url_base = "https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="

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
        
        "Product Name",
        "Price",
        "Ratings",
        "camera_details",
        "battery_details",
        "Processor",
        "product_color",
        "model_name",
        "display_size",
        "display_type",
        "resolution",
        "operating_system",
        "processor_type",
        "ram_size",
        "internal_storage",
        "Product_Url"
    ])

    # Loop through each product on the page
    for product in range(len(product_links)):
        # Get the content of the product page
        product_url = product_links[product]
        product_content = url_content(product_url)

        # Get the product details and store them in a data frame
        product_names = get_product_name(product_content)
        product_prices = get_product_price(product_content)
        product_ratings = get_product_ratings(product_content)
        camera_detailss = get_camera_features(product_content)
        battery_detailss = get_battery_details(product_content)
        processors = get_processor(product_content)
        product_colors = get_product_color(product_content)
        model_names = get_model_name(product_content)
        display_sizes = get_display_size(product_content)
        display_types = get_display_type(product_content)
        resolutions = get_resolution(product_content)
        operating_systems = get_operating_system(product_content)
        processor_types = get_processor_type(product_content)
        ram_sizes = get_ram_size(product_content)
        internal_storages = get_internal_storage(product_content)

        df = pd.DataFrame({
            "Product Name": product_names,
            "Price": product_prices,
            "Ratings": product_ratings,
            "camera_details": camera_detailss,
            "battery_details": battery_detailss,
            "Processor": processors,
            "product_color": product_colors,
            "model_name": model_names,
            "display_size": display_sizes,
            "display_type": display_types,
            "resolution": resolutions,
            "operating_system": operating_systems,
            "processor_type": processor_types,
            "ram_size": ram_sizes,
            "internal_storage": internal_storages,
            "Product_Url": product_url
        })

        data = pd.concat([data, pd.DataFrame.from_dict(df)], ignore_index=True)

    # Add the data frame to the list of data frames
    df_list.append(data)

# Concatenate all the data frames in the list into a single data frame
final_df = pd.concat(df_list, ignore_index=True)

# Export the data frame as a CSV file
final_df.to_csv("smartphone_data.csv", index=False)



