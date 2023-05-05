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


#Function for  name of water purifier filter

def get_product_name(soup):
    product_name = []
    try:
        name = soup.find('span', attrs={'class': "B_NuCI"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    # product_name = "Product Name"
    return product_name

#Function for  prices of water purifier filter

def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div', attrs={'class': "_30jeq3 _16Jk6d"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price

#Function for ratings of water purifier filter

def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs={'class': '_3LWZlK'}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings

#Function for micron rating of water purifier filter

def get_micron_rating(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        micron_rating = [spec[0].split(': ')[1] for spec in specifications]
    except:
        micron_rating = "No rating available"
    return micron_rating

##Function for filtration stages of water purifier filter

def get_filtration_stages(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        filtration_stages = [spec[2] for spec in specifications]
    except:
        filtration_stages = "NO value available"
    return filtration_stages

#Function for shelf life of water purifier filter

def get_shelf_life(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        shelf_life = [spec[3] for spec in specifications]
    except:
        shelf_life = "NO value available"
    return shelf_life

#Function for best suited water filters

def get_best_suited_purifiers(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        best_suited_purifiers = [spec[4] for spec in specifications]
    except:
        best_suited_purifiers = "NO value available"
    return best_suited_purifiers

#Function for filter material of water purifier filter

def get_filter_material(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        filter_material = [spec[4] for spec in specifications]
    except:
        filter_material = "NO value available"
    return filter_material

#Function for compatible with other purifiers

def get_compatible_with(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        compatible_with_purifiers = [spec[1] for spec in specifications]
    except:
        compatible_with_purifiers = "NO value available"
    return compatible_with_purifiers

#Function for number of pack of water purifier filter

def get_number_of_packs(soup):
    specifications=[]
    for item in soup.find_all("div", class_="_2418kt"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="_21Ahn-")]
            specifications.append(item_specifications)
    try:
        no_of_packs = [spec[1] for spec in specifications]
    except:
        no_of_packs = "NO value available"
    return no_of_packs


# Define the URL

url_base = "https://www.flipkart.com/search?q=water+purifier+filter&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
# Create an empty list to store data frames

df_list = []

# Scraping 
for page in range(1,40):
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
        "Micron Ratings",
        "Number of Filtration Stages",
        "Shelf Life",
        "Best Suited Purifiers",
        "Filter Material",
        "Compatible with other purifiers",
        "Number of Packs",
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
        product_ratings= get_product_ratings(product_content)
        micron_ratings = get_micron_rating(product_content)
        filtration_stage = get_filtration_stages(product_content)
        shelf_lifes = get_shelf_life(product_content)
        best_suited_purifiers = get_best_suited_purifiers(product_content)
        filter_material = get_filter_material(product_content)
        compatible_with_others = get_compatible_with(product_content)
        no_of_packs = get_number_of_packs(product_content)
        
        df = pd.DataFrame({
            "Product Name": product_names,
            "Price": product_prices,
            "Ratings" : product_ratings,
             "Micron Ratings" : micron_ratings,
            "Number of Filtration Stages" : filtration_stage,
            "Shelf Life" : shelf_lifes,
            "Best Suited Purifiers" : best_suited_purifiers,
            "Filter Material" : filter_material,
            "Compatible with other purifiers" : compatible_with_others ,
            "Number of Packs" : no_of_packs,
            "Product_Url" :product_url

            
        })
        

        data = pd.concat([data, pd.DataFrame.from_dict(df)], ignore_index=True)

    # Add the data frame to the list of data frames
    df_list.append(data)

# Concatenate all the data frames in the list into a single data frame
final_df = pd.concat(df_list, ignore_index=True)

# Export the data frame as a CSV file
final_df.to_csv("water purifier filter.csv", index=False)



