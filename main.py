from bs4 import BeautifulSoup
import requests
from const import *


def load_pages():
    for page_number in range(129, 3477):
        page = requests.get(f"{URL}/recepty?page={page_number}")
        if page.status_code != 200:
            print("error")
        with open(f'/home/bigcubecat/pages/{page_number}.html', 'w') as f:
            f.write(page.text)


load_pages()
'''
soup = BeautifulSoup(page.text, "html.parser")
page_recipes = soup.findAll('a', class_="emotion-18hxz5k")
for data in page_recipes:
    if data.find('span', class_="emotion-1j2opmb"):
        print(data)
    else:
        print("lol")
'''
