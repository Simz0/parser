import requests
from const import *

if __name__ == "__main__":
    for rec in open('result.txt'):
        obj = eval(rec)
        with open(f'recipes/{obj[0]}.html', 'w') as f:
            page = requests.get(f"{URL}{obj[1]}")
            if page.status_code != 200:
                print("error: ", page.status_code)
            else:
                f.write(page.text)
