from bs4 import BeautifulSoup
import requests

ingrid = []
url = input()
page = requests.get(url)

kasha = BeautifulSoup(page.text, "html.parser")
allingrid = kasha.findAll('span', itemprop="recipeIngredient")

print(allingrid)
for ing in allingrid:
    ingrid.append(ing.text)
    
print(ingrid)

namet = []
name = kasha.findAll('h1', class_="emotion-gl52ge")
for data in name:
    namet.append(data.text)
    
print(namet)  # тут есть проблема, так как на некоторых названиях происходит баг :/
