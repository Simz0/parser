from bs4 import BeautifulSoup
import requests

url = "https://eda.ru/recepty"
page = requests.get(url)
print(page.status_code)
namereciptes = []
reciptes = []
soup = BeautifulSoup(page.text, "html.parser")
allreciptes = soup.findAll('a', class_="emotion-18hxz5k")
print(allreciptes)
for data in allreciptes:
    if data.find('span', class_="emotion-1j2opmb"):
        namereciptes.append(data.text)
print(namereciptes)
for data in namereciptes:
    print(data)
