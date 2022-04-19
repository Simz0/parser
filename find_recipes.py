from bs4 import *


def get_page_recipes(page_text: str):
    soup = BeautifulSoup(page_text, "html.parser")
    all_recipes = soup.findAll('a', class_="emotion-18hxz5k")
    result = []
    for data in all_recipes:
        if data.find('span', class_="emotion-1j2opmb"):
            result.append(str((data.text, data.attrs["href"])))
    return result


if __name__ == "__main__":
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
