import pytest

from src.category import Category
from src.lawngrass_product import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone_product import Smartphone


@pytest.fixture()
def first_product():
    return Product(
        name="hyundai i20",
        description="""Cубкомпактный хетчбэк, выпускающийся с 2008 года. В большинстве стран Hyundai i20 пришёл
        на смену модели Getz""",
        price=1700000,
        quantity=5,
    )


@pytest.fixture()
def first_category():
    return Category(
        name="автомобили",
        description="""Самодвижущееся транспортное средство с двигателем для перевозки грузов и пассажиров
         по безрельсовым путям""",
        products=["Hyundai i20", "Lada Vesta", "Daewoo Matiz"],
    )


@pytest.fixture()
def second_category():
    return Category(
        name="стрелковое оружие",
        description="""орудия (изделия), для стрельбы, изготовленные человеком для добычи зверя, развлечения (спорт),
         борьбы со своим противником или иного.""",
        products=[
            'Ружье служебное "Сайга-410СВ" калибра 410/76',
            'Ружье служебное многозарядное "Бекас-12М" калибра 12/70',
            'Карабин служебный самозарядный "Вепрь-12С Молот" (ВПО-205С) калибра 12/76',
        ],
    )


@pytest.fixture()
def add_product_in_category():
    return Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture()
def third_product():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture()
def second_product():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture()
def fist_product_for_add():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture()
def second_product_for_add():
    return Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture()
def product_iterator(second_category):
    return ProductIterator(second_category)


@pytest.fixture()
def product_smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture()
def product_smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture()
def product_lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def product_lawngrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture()
def category_without_products():
    return Category(
        name="боевое оружие",
        description="Оружие войны",
        products= []
    )