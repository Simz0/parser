from bs4 import BeautifulSoup
import requests

ingrid=[]
url="https://eda.ru/recepty/zavtraki/sirniki-iz-tvoroga-18506"
page=requests.get(url)

kasha=BeautifulSoup(page.text, "html.parser")
allingrid=kasha.findAll('span', itemprop="recipeIngredient")

print(allingrid)
for ing in allingrid:
    ingrid.append(ing.text)
print(ingrid)
'''
for data in allingrid:
    if data.find('span',itemprop_="recipeIngredient"):
        ingrid.append(data.text)
print(ingrid)
'''