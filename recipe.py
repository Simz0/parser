# emotion-1x1q7i2
from bs4 import *
import os
from utils import *

for filename in os.listdir('recipes'):
    with open(f'recipes/{filename}') as f:
        page_text = '\n'.join(f.readlines())
    title = filename.replace(".html", "")
    description = get_description(page_text)
    ingredients = get_ingredients(page_text)
    energy = get_energy(page_text)
    steps = get_steps(page_text)
