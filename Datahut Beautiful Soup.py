#!/usr/bin/env python
# coding: utf-8

# In[60]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

 


# In[61]:


url = "https://www.flipkart.com/search?q=smartphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&as-pos=1&as-type=HISTORY&suggestionId=smartphone%7CMobiles&requestId=2dad4d82-e2ba-4086-a738-d902a82005b2"


# In[62]:


req = requests.get(url)
content = BeautifulSoup(req.content,'lxml')


# In[63]:


data = content.find_all('div',{'class' : "_2kHMtA"})


# In[64]:


print(data)


# In[65]:


links = []
phn_name = []
price = []
rating = []
about_the_phone = []
start_link = "https://www.flipkart.com/"


# In[66]:


for items in data:
    rest_link = items.find('a')['href']
    name = items.find('div',attrs={'class':"_4rR01T"})
    phn_name.append(name.text)
    links.append(start_link+rest_link)
    prices=items.find('div', attrs={'class':"_30jeq3 _1_WHN1"})
    price.append(prices.text)
    ratings=items.find('div',attrs={'class':"_3LWZlK"})
    rating.append(ratings.text)
    about_the_phones=items.find('li',attrs={'class':"rgWa7D"})
    about_the_phone.append(about_the_phones.text)



# In[67]:


print(phn_name)


# In[68]:


len(phn_name)


# In[69]:


print(links)


# In[70]:


dataframe={'Phone_names':phn_name, 'Links':links, 'price': price,'ratings':rating,'Supported_apps':apps,'sound_system':sound,'OS':os,"Resolution":hd}
Final_dataframe=pd.DataFrame(dataframe)
print(Final_dataframe)


# In[71]:


print(price)


# In[72]:


len(price)


# In[73]:


#print(len(products))
print(len(ratings))
print(len(prices))
print(len(apps))
print(len(sound))
print(len(os))
#print(len(had))


# In[ ]:





# In[ ]:





# In[ ]:


len(phn_name)


# In[ ]:


len(links)


# In[ ]:


len(rating)


# In[ ]:


Final_dataframe.to_json


# In[ ]:


with open('Final_dataframe.json', 'w') as file:
     json.dump(Final_dataframe, file)


# In[ ]:


import json


# In[ ]:





# In[ ]:





# In[ ]:


print(rating)


# In[25]:


print(about_the_phone)


# In[27]:


print(about_the_phone[2])


# In[74]:


specification=items.find('div',class_="fMghEO")
print(specification)
specification.text


# In[37]:


for each in about_the_phone:
    spec=items.find_all('li',class_='rgWa7D')
    print(spec[0].text)
    print(spec[1].text)
    print(spec[2].text)
    print(spec[3].text)
    print(spec[4].text)
    print(spec[5].text)


# In[ ]:


len(about_the_phone)


# In[41]:


apps = []                #List to store supported apps                
os = []                  #List to store operating system
hd = []                  #List to store resolution
sound = []               #List to store sound output


# In[42]:


for each in specification:
           col=each.find_all('li', attrs={'class':'rgWa7D'})
           app =col[0].text
           os_ = col[1].text
           hd_ = col[2].text
           sound_ = col[3].text


# In[48]:


#products.append(names.text) # Add product name to list
           #prices.append(price.text) # Add price to list
apps.append(app)# Add supported apps specifications to list
os.append(os_) # Add operating system specifications to list
hd.append(hd_) # Add resolution specifications to list
sound.append(sound_) # Add sound specifications to list
#ratings.append(rating.text)   #Add rating specifications to list


# In[ ]:


import pandas as pd
df=pd.DataFrame({'Product Name':products,'Supported_apps':apps,'sound_system':sound,'OS':os,"Resolution":hd,'Price':prices,'Rating':ratings})
df.head(10)


# In[58]:


print(os)


# In[59]:


print(apps)


# In[ ]:





# In[ ]:





# In[ ]:


Television


# In[ ]:


url = 'https://www.flipkart.com/search?q=television&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'


# In[ ]:


req2 = requests.get(url)
content2 = BeautifulSoup(req2.content,'lxml')


# In[ ]:


print(content2)


# In[ ]:





# In[ ]:


data2 = content2.find_all('div',{'class' : "_2kHMtA"})


# In[ ]:


print(data2)


# In[ ]:


television_name=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
apps = []                #List to store supported apps                
os = []                  #List to store operating system
hd = []                  #List to store resolution
sound = []               #List to store sound output


# In[ ]:


for items in data2:
   
    television_name = items.find('div',attrs={'class':"_4rR01T"})
    phn_name.append(name.text)
    links.append(start_link+rest_link)
    prices=items.find('div', attrs={'class':"_30jeq3 _1_WHN1"})
    price.append(prices.text)
    ratings=items.find('div',attrs={'class':"_3LWZlK"})
    rating.append(ratings.text)
    about_the_phones=items.find('li',attrs={'class':"rgWa7D"})
    about_the_phone.append(about_the_phones.text)


# In[ ]:


names=data2.find('div', attrs={'class':'_4rR01T'})
price=data2.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
rating=data2.find('div', attrs={'class':'_3LWZlK'})
specification = data2.find('div', attrs={'class':'fMghEO'})


# In[ ]:


prices=items.find('div', attrs={'class':"_30jeq3 _1_WHN1"})
price.append(prices.text)
ratings=items.find('div',attrs={'class':"_3LWZlK"})
rating.append(ratings.text)
about_the_phones=items.find('li',attrs={'class':"rgWa7D"})
about_the_phone.append(about_the_phones.text)

   


# In[ ]:


Final_dataframe.to_json


# In[ ]:


# sample dataframe
#Final_dataframe = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

# convert to JSON
Final_dataframe_json =Final_dataframe.to_json(orient='records')

print(Final_dataframe_json)


# In[ ]:


with open('Final_dataframe_json.json', 'w') as file:
     json.dump(Final_dataframe_json, file)


# In[11]:


specifications = items.find_all('li', class_='_3YhLQA')

for spec in specifications:
    print(spec.text)


# In[13]:


print(spec)


# In[38]:


print(about_the_phone)


# In[ ]:




