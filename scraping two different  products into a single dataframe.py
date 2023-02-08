import requests
from bs4 import BeautifulSoup
import pandas as pd

products=[]
prices=[]
ratings=[]
results=[]


urls=['https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off',
     'https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_2_0_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_2_0_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=laptops&requestId=3df6e11f-d4d4-41be-a3f4-bd5fe4faacd7',
     ]

for url in urls:
    def scrape_flipkart_product_info(url):
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):

            name = a.find("div", {"class": "_4rR01T"})
            rating = a.find("div", {"class": "_3LWZlK"})
            price = a.find("div", {"class": "_30jeq3 _1_WHN1"})
            # products.append(name.get_text()) if name else 'No product name available'
            # prices.append(price.get_text()) if price else 'No rating available'

            # including missing product_name
            if name:
                name1 = name.text
            else:
                name1 = "No rating available"
            if name1:
                products.append(name1)
            else:
                products.append("No rating available")

            # including missing price
            if price:
                price1 = price.text
            else:
                price1 = "No rating available"
            if price1:
                prices.append(price1)
            else:
                prices.append("No rating available")

            # including missing  ratings
            if rating:
                rating1 = rating.text
            else:
                rating1 = "No rating available"
            if rating1:
                ratings.append(rating1)
            else:
                ratings.append("No rating available")

        return (
            products,
            ratings,
            prices,
        )


    products, ratings, prices = scrape_flipkart_product_info(url)
    results.append({
        "Product Name": products,
        "Rating": ratings,
        "Price": prices})

    # Getting pandas dataframe
df = pd.DataFrame({'Product': products, 'Price': prices, 'Ratings': ratings})
df.head()


df.shape
