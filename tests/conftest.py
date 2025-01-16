import pytest

from src.category import Category
from src.product import Product


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
    return Product(
        name="55\" QLED 4K",
        description="Фоновая подсветка",
        price=123000.0,
        quantity=7
    )

@pytest.fixture()
def third_product():
    return {
        'name': "Samsung Galaxy S23 Ultra",
        'description': "256GB, Серый цвет, 200MP камера",
        'price': 180000.0,
        'quantity': 5
        }
