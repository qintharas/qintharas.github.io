import requests
from bs4 import BeautifulSoup
import json
import datetime


data_headline = {}

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, "html.parser")
data=[]


for headline in obj.find_all('div', class_='conten1'):
        
    currentDT = datetime.datetime.now()
    x = headline.find('h1').text
    y = headline.find('h2').text
    z = currentDT.strftime("%d %b %Y %H:%M:%S")
    q = headline.find('div',class_='date').text
    data_headline['cat'] = x
    data_headline['title'] = y
    data_headline['gettime'] = z
    data_headline['timepublished']= q
        
    data.append (dict(data_headline))

data_headline = data        
with open('dataheadline.json', 'w') as file:
    json.dump(data_headline, file, indent=4)
