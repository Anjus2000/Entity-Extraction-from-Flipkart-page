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
    for item in soup.find_all('a',href=True, attrs={'class':'_2UzuFa'}):
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


#Function for product model name

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

#Function for dial colour

def get_dial_color(soup):
    dial_color = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "dial color":
                dial_color = cells[1].text.strip()
                break
        if not dial_color:
            dial_color = "No value available"
    except:
        dial_color = "No value available"
    return dial_color

#function for dial shape

def get_dial_shape(soup):
    dial_shape = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "dial shape":
                dial_shape = cells[1].text.strip()
                break
        if not dial_shape:
            dial_shape = "No value available"
    except:
        dial_shape = "No value available"
    return dial_shape

#Function for strap colour

def get_strap_color(soup):
    strap_color = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "strap color":
                strap_color = cells[1].text.strip()
                break
        if not strap_color:
            strap_color = "No value available"
    except:
         strap_color = "No value available"
    return strap_color

#Function for strap material

def get_strap_material(soup):
    strap_material = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "strap material":
                strap_material = cells[1].text.strip()
                break
        if not strap_material:
            strap_material = "No value available"
    except:
         strap_material = "No value available"
    return strap_material

#Function for size

def get_size(soup):
    size = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[0]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "size":
                size = cells[1].text.strip()
                break
        if not size:
            size = "No value available"
    except:
         size = "No value available"
    return size

#Function for touchscreen

def get_touchscreen(soup):
    touchscreen = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[0]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "touchscreen":
                touchscreen = cells[1].text.strip()
                break
        if not touchscreen:
            touchscreen = "No value available"
    except:
         touchscreen = "No value available"
    return touchscreen

#Function for water resistant

def get_water_resistant(soup):
    water_resistant = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[0]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "water resistant":
                water_resistant = cells[1].text.strip()
                break
        if not water_resistant:
            water_resistant = "No value available"
    except:
         water_resistant = "No value available"
    return water_resistant

#Function for water resistance depth

def get_water_resistance_depth(soup):
    water_resistance_depth = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[0]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "water resistance depth":
                water_resistance_depth = cells[1].text.strip()
                continue
        if not water_resistance_depth:
            water_resistance_depth = "No value available"
    except:
         water_resistance_depth = "No value available"
    return water_resistance_depth


#Function for dial material

def get_dial_material(soup):
    dial_material = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[0]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "dial material":
                dial_material = cells[1].text.strip()
                continue
        if not dial_material:
             dial_material = "No value available"
    except:
         dial_material = "No value available"
    return dial_material

#Function for ideal for (men or women)

def get_ideal_for(soup):
    ideal_for = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[0]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "ideal for":
                ideal_for = cells[1].text.strip()
                continue
        if not ideal_for:
             ideal_for = "No value available"
    except:
         ideal_for = "No value available"
    return ideal_for

#function for compatible os

def get_compatible_os(soup):
    compatible_os = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[0]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "compatible os":
                compatible_os = cells[1].text.strip()
                continue
        if not compatible_os:
             compatible_os = "No value available"
    except:
         compatible_os = "No value available"
    return compatible_os

# Function for sensor

def get_sensor(soup):
    sensor = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "sensor":
                sensor = cells[1].text.strip()
                continue
        if not sensor:
             sensor = "No value available"
    except:
         sensor = "No value available"
    return sensor

#function for compatible device

def get_compatible_device(soup):
    compatible_device = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "compatible device":
                compatible_device = cells[1].text.strip()
                continue
        if not compatible_device:
             compatible_device = "No value available"
    except:
         compatible_device = "No value available"
    return compatible_device

#Function for notification

def get_notification(soup):
    notification = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "notification":
                notification = cells[1].text.strip()
                continue
        if not notification:
             notification = "No value available"
    except:
         notification = "No value available"
    return notification

#Function for charge time

def get_charge_time(soup):
    charge_time = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "charge time":
                charge_time = cells[1].text.strip()
                continue
        if not charge_time:
             charge_time = "No value available"
    except:
         charge_time = "No value available"
    return charge_time

#function for battery life

def get_battery_life(soup):
    battery_life = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "battery life":
                battery_life = cells[1].text.strip()
                continue
        if not battery_life:
             battery_life = "No value available"
    except:
         battery_life = "No value available"
    return battery_life

#Function for charger type

def get_charger_type(soup):
    charger_type = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[1]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "charger type":
                charger_type = cells[1].text.strip()
                continue
        if not charger_type:
             charger_type = "No value available"
    except:
         charger_type = "No value available"
    return charger_type

#Function for display resolution

def get_display_resolution(soup):
    display_resolution = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "display resolution":
                display_resolution = cells[1].text.strip()
                continue
        if not display_resolution:
             display_resolution = "No value available"
    except:
         display_resolution = "No value available"
    return display_resolution

#Functuion for display size

def get_display_size(soup):
    display_size = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "display size":
                display_size = cells[1].text.strip()
                continue
        if not display_size:
             display_size = "No value available"
    except:
         display_size = "No value available"
    return display_size

#Function for display type

def get_display_type(soup):
    display_type = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[3]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "display type":
                display_type = cells[1].text.strip()
                continue
        if not display_type:
             display_type = "No value available"
    except:
         display_type = "No value available"
    return display_type

#function for call features

def get_call_features(soup):
    call_features = ""
    try:
        table = soup.find_all("div", {"class": "_3k-BhJ"})[2]
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "call features":
                call_features = cells[1].text.strip()
                continue
        if not call_features:
             call_features = "No value available"
    except:
         call_features = "No value available"
    return call_features


# Define the URL
url_base = "https://www.flipkart.com/search?q=smart%20watch&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
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
        "Model Name",
        "Dial Color",
        "Dial Shape",
        "Strap Color",
        "Strap Material",
        "Size",
        "Touchscreen",
        "Water Resistant",
        "Water Resistance Depth",
        "Dial Material",
        "Ideal For",
        "Compatible OS",
        "Sensor",
        "Compatible Device",
        "Notification",
        "Charge Time",
        "Battery Life",
        "Charger Type",
        "Display Resolution",
        "Display Size",
        "Display Type",
        "Call Features",
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
        model_name = get_model_name(product_content)
        dial_color = get_dial_color(product_content)
        dial_shape = get_dial_shape(product_content)
        strap_color = get_strap_color(product_content)
        strap_material = get_strap_material(product_content)
        size = get_size(product_content)
        touchscreen = get_touchscreen(product_content)
        water_resistant = get_water_resistant(product_content)
        water_resistance_depth = get_water_resistance_depth(product_content)
        dial_material = get_dial_material(product_content)
        ideal_for = get_ideal_for(product_content)
        compatible_os = get_compatible_os(product_content)
        sensor = get_sensor(product_content)
        compatible_device = get_compatible_device(product_content)
        notification = get_notification(product_content)
        charge_time = get_charge_time(product_content)
        battery_life = get_battery_life(product_content)
        charger_type = get_charger_type(product_content)
        display_resolution = get_display_resolution(product_content)
        display_size = get_display_size(product_content)
        display_type = get_display_type(product_content)
        call_features = get_call_features(product_content)
        
        df = pd.DataFrame({
            "Product Name": product_name,
            "Price": product_price,
            "Ratings": product_ratings,
            "Model Name": model_name,
            "Dial Color": dial_color,
            "Dial Shape": dial_shape,
            "Strap Color": strap_color,
            "Strap Material": strap_material,
            "Size": size,
            "Touchscreen": touchscreen,
            "Water Resistant": water_resistant,
            "Water Resistance Depth": water_resistance_depth,
            "Dial Material": dial_material,
            "Ideal For": ideal_for,
            "Compatible OS": compatible_os,
            "Sensor": sensor,
            "Compatible Device": compatible_device,
            "Notification": notification,
            "Charge Time": charge_time,
            "Battery Life": battery_life,
            "Charger Type": charger_type,
            "Display Resolution": display_resolution,
            "Display Size": display_size,
            "Display Type": display_type,
            "Call Features": call_features,
            "Product_Url":product_url

            
        })
        

        data = pd.concat([data, pd.DataFrame.from_dict(df)], ignore_index=True)

    # Add the data frame to the list of data frames
    df_list.append(data)

# Concatenate all the data frames in the list into a single data frame
final_df = pd.concat(df_list, ignore_index=True)

# Export the data frame as a CSV file
final_df.to_csv("Smartwatch.csv", index=False)






