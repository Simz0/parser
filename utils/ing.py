from bs4 import BeautifulSoup


def get_ingredients(page_text):
    soup = BeautifulSoup(page_text, "html.parser")
    all_ingredients = soup.findAll('span', itemprop="recipeIngredient")
    counts = [i.text.lower() for i in soup.findAll('span', class_='emotion-15im4d2')]
    return [ing.text.lower() for ing in all_ingredients], counts


def get_description(page_text):
    soup = BeautifulSoup(page_text, "html.parser")
    description = soup.find('span', class_="emotion-1x1q7i2")
    if description is None:
        return ""
    return description.text


def get_energy(page_text):
    soup = BeautifulSoup(page_text, "html.parser")
    calories = soup.find('span', itemprop='calories').text
    protein = soup.find('span', itemprop='proteinContent').text
    fat = soup.find('span', itemprop='fatContent').text
    carbohydrate = soup.find('span', itemprop='carbohydrateContent').text
    return [calories, protein, fat, carbohydrate]


def get_steps(page_text):
    soup = BeautifulSoup(page_text, "html.parser")
    steps = soup.findAll('div', itemprop='recipeInstructions')
    steps = [step.text for step in steps]
    return steps
