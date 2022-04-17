import requests
import json


class RecipeObject:
    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description
        self.ingredients = []

    def to_json(self):
        return {
            "title": self.title,
            "link": self.link,
            "description": self.description,
            "ingredients": self.ingredients
        }

    def commit(self, db_url):
        requests.post(url=db_url, json=json.dumps(self.to_json()))
