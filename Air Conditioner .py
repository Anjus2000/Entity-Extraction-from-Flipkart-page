

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


# In[3]:


# Function to extract content from page


# In[4]:


driver = webdriver.Edge()


# In[5]:


def url_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'lxml')
    return soup


# In[6]:


#Function to extract urls of products 


# In[7]:


def get_product_url(soup):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    product_link= []
    start_link = "https://www.flipkart.com"
    for item in soup.find_all('a',href=True, attrs={"_1fQZEK"}):
        rest_link = item['href']
        product_link.append(start_link+rest_link)
    return product_link


# In[8]:


#Function to extract names of products 


# In[9]:


def get_product_name(soup):
    product_name = []
    try:
        name = soup.find('span', attrs={'class': "B_NuCI"}).text
        product_name.append(name)
    except:
        name = "No product name available"
        product_name.append(name)
    return product_name



# In[10]:


#Function to extract price of products 


# In[11]:


def get_product_price(soup):
    product_price = []
    try:
        price = soup.find('div',attrs={'class':"_30jeq3 _16Jk6d"}).text
        product_price.append(price)
    except:
        price = "NO price available"
        product_price.append(price)
    return product_price


# In[12]:


#Function to extract ratings of products 


# In[13]:


def get_product_ratings(soup):
    product_ratings = []
    try:
        ratings = soup.find('div', attrs = {'class':"_3LWZlK"}).text
        product_ratings.append(ratings)
    except:
        ratings = "No rating available"
        product_ratings.append(ratings)
    return product_ratings


# In[14]:


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


# In[15]:


#Function to extract capacity_in_tonsof products 


# In[16]:


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


# In[17]:


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


# In[18]:


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


# In[19]:


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


# In[20]:


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


# In[21]:


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


# In[22]:


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


# In[23]:


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


# In[24]:


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


# In[25]:


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


# In[26]:


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


# In[ ]:





# In[27]:


#Function to extract star_rating of products 


# In[28]:


#Function to extract camera details of products 


# In[29]:


#website_link


# In[30]:


url = "https://www.flipkart.com/search?q=air%20conditioner&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# In[31]:


#Creating dataframe for calculating the length of the dataframe containing the features


# In[32]:


data = pd.DataFrame({"Product_Url":[],"Product Name":[],"Price":[],"Ratings":[],"capacity_in_tons":[],"model_name":[],"product_type":[],"brand":[],"product_color":[],"cooling_capacity":[],"compressor":[],"remote_control":[],"dust_filter":[],"power_consumption":[],"power_requirement":[],"auto_restart":[]})



# In[33]:


url_contents=url_content(url)


# In[34]:


#Getting Each product's link


# In[35]:


product_links=get_product_url(url_contents)







# In[36]:


#Assigning the each product's link to the variaable "Product_Url" in the dataframe


# In[37]:


data["Product_Url"] = product_links



# In[38]:


df = pd.DataFrame()
for page in range(1, 45):
    def assign_to_dataframe(product_content):
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

        df =pd.DataFrame({
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
                "power_requirement":power_requirement
            
            
            })
        
        return df


# In[39]:


for product in range(len(data)): 
    product_url = data["Product_Url"].iloc[product]
    product_content = url_content(product_url)
    df1 = assign_to_dataframe(product_content) 
    df = pd.concat([df, df1], axis=0, ignore_index=True, sort=False)
    df.head()


# In[40]:


df



# In[41]:


smart_phone_json = df.to_json(orient='records')

