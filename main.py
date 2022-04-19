from bs4 import BeautifulSoup
import requests

namereciptes = []
reciptes = []

url = "https://eda.ru/recepty"
page = requests.get(url)
print(page.status_code)


def get_page_recipes(page_text: str):
    soup = BeautifulSoup(page_text, "html.parser")
    allreciptes = soup.findAll('a', class_="emotion-18hxz5k")
    result = []
    for data in allreciptes:
        if data.find('span', class_="emotion-1j2opmb"):
            result.append(str((data.text, data.attrs["href"])))
    return result


for i in range(1, 715):
    page_text = ""
    try:
        with open(f"pages/{i}.html") as f:
            page_text = '\n'.join(f.readlines())
    except Exception as error:
        print(error)
    if page_text != "":
        rec = "\n".join(get_page_recipes(page_text))
        with open('result.txt', 'a') as f:
            f.write(rec)
