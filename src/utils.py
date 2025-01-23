import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    users = []
    for user in data:
        products = []
        for product in user["products"]:
            products.append(Product(**product))
        user["products"] = products
        users.append(Category(**user))
    return users


if __name__ == "__main__":
    raw_data = read_json("../data/data.json")
    users_data = create_objects_from_json(raw_data)
    print(users_data)
    print(users_data[0].name)
    print(users_data[0].products)
