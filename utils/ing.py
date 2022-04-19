from bs4 import BeautifulSoup


def get_ingredients(page_text):
    kasha = BeautifulSoup(page_text, "html.parser")
    all_ingredients = kasha.findAll('span', itemprop="recipeIngredient")
    return [ing.text for ing in all_ingredients]


def get_description(page_text):
    soup = BeautifulSoup(page_text, "html.parser")
    description = soup.find('span', class_="emotion-1x1q7i2")
    if description is None:
        return ""
    return description.text
