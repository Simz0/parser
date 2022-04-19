import requests
from const import *

def load_pages():
    for page_number in range(1000, 3477):
        page = requests.get(f"{URL}recepty?page={page_number}")
        if page.status_code != 200:
            print("error")
        with open(f'pages/{page_number}.html', 'w') as f:
            f.write(page.text)


if __name__ == "__main__":
    load_pages()
