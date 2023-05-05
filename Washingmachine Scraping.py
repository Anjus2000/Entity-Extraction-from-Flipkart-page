


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


#Function to extract brand_name of products 


def get_brand_name(soup):
    brand_name = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "brand":
                brand_name = cells[1].text.strip()
                break
        if not brand_name:
            brand_name = "No value available"
    except:
         brand_name = "No value available"
    return brand_name



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


#Function to extract washing_capacity of products


def get_washing_capacity(soup):
    washing_capacity = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "washing capacity":
                washing_capacity = cells[1].text.strip()
                break
        if not washing_capacity:
            washing_capacity = "No value available"
    except:
         washing_capacity = "No value available"
    return washing_capacity


#Function to extract color of products


def get_color(soup):
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


#Function to extract fuction_type of products


def get_function_type(soup):
    function_type = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "function type":
                function_type = cells[1].text.strip()
                break
        if not function_type:
            function_type = "No value available"
    except:
         function_type = "No value available"
    return function_type


#Function to extract maxmimum spin speed of products


def get_max_spin_speed(soup):
    max_spin_speed = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "maximum spin speed":
                max_spin_speed = cells[1].text.strip()
                break
        if not max_spin_speed:
            max_spin_speed = "No value available"
    except:
        max_spin_speed = "No value available"
    return max_spin_speed



#Function to extract inbuilt_heater of products


def get_inbuilt_heater(soup):
    inbuilt_heater = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "in-built heater":
                inbuilt_heater = cells[1].text.strip()
                break
        if not inbuilt_heater:
            inbuilt_heater = "No value available"
    except:
         inbuilt_heater = "No value available"
    return inbuilt_heater


#Function to extract washing method of products


def get_washing_method(soup):
    washing_method = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "washing method":
                washing_method = cells[1].text.strip()
                break
        if not washing_method:
            washing_method = "No value available"
    except:
         washing_method = "No value available"
    return washing_method




# Define the URL

url_base = "https://www.flipkart.com/search?q=washing%20machine&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
# Create an empty list to store data frames

df_list = []

# Scraping 

for page in range(1,45):
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
        "Brand Name",
        "Model Name",
        "Washing Capacity",
        "Color",
        "Maximum Spin Speed",
        "Function Type",
        "Inbuilt Heater",
        "Washing Method",
        "Product_Url"
       
    ])

    # Loop through each product on the page
    for product in range(len(product_links)):
        # Get the content of the product page
        product_url = product_links[product]
        product_content = url_content(product_url)

        # Get the product details and store them in a data frame
        product_name = get_product_name(product_content)
        product_price = get_product_price(product_content)
        product_ratings = get_product_ratings(product_content)
        brand_name = get_brand_name(product_content)
        model_name = get_model_name(product_content)
        washing_capacity = get_washing_capacity(product_content)
        color = get_color(product_content)
        max_spin_speed = get_max_spin_speed(product_content)
        function_type = get_function_type(product_content)
        inbuilt_heater = get_inbuilt_heater(product_content)
        washing_method = get_washing_method(product_content)


        df = pd.DataFrame({
             "Product Name": product_name,
             "Price": product_price,
             "Ratings" : product_ratings,
             "Brand Name": brand_name,
             "Model Name": model_name,
             "Washing Capacity": washing_capacity,
             "Color": color,
             "Maximum Spin Speed":max_spin_speed,
             "Function Type":function_type,
             "Inbuilt Heater": inbuilt_heater,
             "Washing Method": washing_method,
             "Product_Url": product_url


             })
        

        data = pd.concat([data, pd.DataFrame.from_dict(df)], ignore_index=True)

    # Add the data frame to the list of data frames
    df_list.append(data)

# Concatenate all the data frames in the list into a single data frame
final_df = pd.concat(df_list, ignore_index=True)

# Export the data frame as a CSV file
final_df.to_csv("Washingmachine.csv", index=False)


# In[ ]:





# In[ ]:




