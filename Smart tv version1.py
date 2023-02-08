#importing necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

#defining the lists to store the value of each feature
product_name=[]
price=[]
ratings=[]
results=[]
specifications=[]

# Choose the data you need to extract
urls=['https://www.flipkart.com/search?q=smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&as-pos=1&as-type=HISTORY&suggestionId=smart+tv%7CTelevisions&requestId=ac4665a8-c1ef-462b-9fb8-e5913908cc39']



#scraping data
for url in urls:
    def scrape_flipkart_product_info(url):
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        for item in soup.find_all("div", class_="fMghEO"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="rgWa7D")]
            specifications.append(item_specifications)
        operating_systems = [spec[0].split(': ')[1] for spec in specifications]
        resolutions = [spec[1] for spec in specifications]
        warranties = [spec[2] for spec in specifications]

        for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):

            name = a.find("div", {"class": "_4rR01T"})
            rating = a.find("div", {"class": "_3LWZlK"})
            prices = a.find("div", {"class": "_30jeq3 _1_WHN1"})

            product_name.append(name.text)
            price.append(prices.text)

            try:
                ratings.append(rating.text)
            except:
                ratings.append("No rating available")

        return (
            product_name, price, ratings, operating_systems, resolutions, warranties
        )


    for i in range(1, 3):
        url = f"https://www.flipkart.com/search?q=smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_5_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=smart+tv%7CTelevisions&requestId=f2b6d844-2ae5-494f-a3b4-712fe4a6821d&as-backfill=on"
        products, price, ratings, operating_systems, resolutions, warranties = scrape_flipkart_product_info(url)
        results.append({
            "Product Name": product_name,
            "Price": price,
            "Rating": ratings,
            "Operating System": operating_systems,
            "Resolution": resolutions,
            "Warranty": warranties,
        })

    #storing the data into the structured format in the dataframe
df = pd.DataFrame(
        {'Product Name': product_name, 'Price': price, 'Ratings': ratings, "Operating System": operating_systems,
         "Resolution": resolutions, "Warranty": warranties})
df.head()
