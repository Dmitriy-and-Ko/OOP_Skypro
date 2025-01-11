
class Category:
    name: str
    description: str
    products: list
    category_quantity = 0
    products_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_quantity += 1
        Category.products_quantity += len(products)