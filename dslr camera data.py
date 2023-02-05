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
urls=['https://www.flipkart.com/search?q=dslr+camera&as=on&as-show=on&otracker=AS_Query_PredictiveAutoSuggest_5_0_na_na_na&otracker1=AS_Query_PredictiveAutoSuggest_5_0_na_na_na&as-pos=5&as-type=PREDICTIVE&suggestionId=dslr+camera&requestId=1effde04-d2f3-4a7b-98b8-106a1d986a19']


#scraping data
for url in urls:
    def scrape_flipkart_product_info(url):
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        for item in soup.find_all("div", class_="fMghEO"):
            item_specifications = [spec.text for spec in item.find_all("li", class_="rgWa7D")]
            specifications.append(item_specifications)

        warranty = [spec[-1].split(': ')[-1] for spec in specifications]
        sensor_type = [spec[-2] for spec in specifications]
        wifi_availability = [spec[-3] for spec in specifications]
        resolution = [spec[-4] for spec in specifications]
        effective_pixels = [spec[-5].split(':')[1] for spec in specifications]

        # eff- ses, ses- reso, reso- effe, wifi_availability- sens

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
            product_name, price, ratings, warranty, effective_pixels, sensor_type, wifi_availability, resolution
        )


    for i in range(1, 3):
        url = f"https://www.flipkart.com/search?q=dslr+camera&as=on&as-show=on&otracker=AS_Query_PredictiveAutoSuggest_5_0_na_na_na&otracker1=AS_Query_PredictiveAutoSuggest_5_0_na_na_na&as-pos=5&as-type=PREDICTIVE&suggestionId=dslr+camera&requestId=1effde04-d2f3-4a7b-98b8-106a1d986a19"
        products, price, ratings, warranty, effective_pixels, resolution, wifi_availability, sensor_type, = scrape_flipkart_product_info(
            url)
        results.append({
            "Product Name": product_name,
            "Price": price,
            "Rating": ratings,
            "Wifi Availability": wifi_availability,
            "Sensor Type": sensor_type,
            "Resolution": resolution,
            "Warranty": warranty,
            "Effective Pixels": effective_pixels
        })


#storing the data into the structured format in the dataframe
df=pd.DataFrame({'Product Name':product_name,'Price':price,'Ratings':ratings,"Resolution" : resolution ,  "Effective Pixels" : effective_pixels,   "Sensor Type"  : sensor_type, "Wifi Availability":wifi_availability,"Warranty":warranty})
df.head()