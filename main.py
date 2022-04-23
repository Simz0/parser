import json
import os

import requests

from utils import *


def log(data):
    with open('log', 'a') as log_file:
        log_file.write(data)


FOLDER = 'recipes'

if __name__ == "__main__":
    recipes = {}
    for obj in open('result.txt'):
        k, v = eval(obj)
        recipes[k] = v
    for filename in os.listdir(FOLDER):
        with open(f'{FOLDER}/{filename}') as f:
            page_text = '\n'.join(f.readlines())
        title = filename.replace(".html", "")
        description = get_description(page_text)
        ingredient_titles, counts = get_ingredients(page_text)
        energy = ';'.join(get_energy(page_text))  # соеденины ;
        steps = ';'.join(get_steps(page_text))
        counts_json = {}
        for i, e in enumerate(counts):
            counts_json[ingredient_titles[i]] = e
        link = recipes[title]
        print(ingredient_titles)
        new_recipe = {
            "title": title,
            "description": description,
            "energy": energy,
            "steps": steps,
            "ingredients": ingredient_titles,
            "counts": json.dumps(counts_json),
            "link": link
        }
        response = requests.post('http://127.0.0.1:8080/add', json=new_recipe)
        print(new_recipe)
        print(response.text)
