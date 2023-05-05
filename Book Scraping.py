#!/usr/bin/env python
# coding: utf-8

# In[18]:


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
    for item in soup.find_all('a',href=True, attrs={'class':'s1Q9rs'}):
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


#Function to extract author of products 

def get_author(soup):
    author = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "author":
                author = cells[1].text.strip()
                break
        if not author:
            author = "No value available"
    except:
         author = "No value available"
    return author


#Function to extract publising date of products 


def get_publishing_date(soup):
    publishing_date = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "publication date":
                publishing_date = cells[1].text.strip()
                break
        if not publishing_date:
            publishing_date = "No value available"
    except:
         publishing_date = "No value available"
    return publishing_date



#Function to extract publisher of products 


def get_publisher(soup):
    publisher = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "publisher":
                publisher = cells[1].text.strip()
                break
        if not publisher:
            publisher = "No value available"
    except:
         publisher = "No value available"
    return publisher


#Function to extract edition of products 


def get_edition(soup):
    edition = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "edition":
                edition = cells[1].text.strip()
                break
        if not edition:
            edition = "No value available"
    except:
        edition = "No value available"
    return edition


#Function to extract number of pages of products 


def get_number_of_pages(soup):
    pages = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "number of pages":
                pages = cells[1].text.strip()
                break
        if not pages:
            pages = "No value available"
    except:
         pages = "No value available"
    return pages

#Function to extract language of products 


def get_language(soup):
    language = ""
    try:
        table = soup.find("div", {"class": "_3k-BhJ"})
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells[0].text.strip().lower() == "language":
                language = cells[1].text.strip()
                break
        if not language:
            language = "No value available"
    except:
         language = "No value available"
    return language









# Define the URL

url_base = "https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
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
        "Author",
        "Publishing Date",
        "Publisher",
        "Edition",
        "Number of Pages",
        "Language",
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
        author = get_author(product_content)
        publishing_date = get_publishing_date(product_content)
        publisher = get_publisher(product_content)
        edition = get_edition(product_content)
        pages = get_number_of_pages(product_content)
        language = get_language(product_content)


        df = pd.DataFrame({
             "Product Name": product_name,
             "Price": product_price,
             "Ratings": product_ratings,
             "Author": author,
             "Publishing Date": publishing_date,
             "Publisher": publisher,
             "Edition": edition,
             "Number of Pages": pages,
             "Language": language,
             "Product_Url": product_url


             })
        

        data = pd.concat([data, pd.DataFrame.from_dict(df)], ignore_index=True)

    # Add the data frame to the list of data frames
    df_list.append(data)

# Concatenate all the data frames in the list into a single data frame
final_df = pd.concat(df_list, ignore_index=True)

# Export the data frame as a CSV file
final_df.to_csv("Book.csv", index=False)


# In[ ]:




