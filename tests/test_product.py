from src.category import Category, product1, product3
from src.product import Product
from tests.conftest import first_category, first_product


def test_product_init(first_product):
    assert first_product.name == "hyundai i20"
    assert (
        first_product.description
        == """Cубкомпактный хетчбэк, выпускающийся с 2008 года. В большинстве стран Hyundai i20 пришёл
        на смену модели Getz"""
    )
    assert first_product.price == 1700000
    assert first_product.quantity == 5


def test_product_new_product(third_product):
    assert Product.new_product(third_product).name == "Samsung Galaxy S23 Ultra"
    assert Product.new_product(third_product).description == "256GB, Серый цвет, 200MP камера"
    assert Product.new_product(third_product).price == 180000.0
    assert Product.new_product(third_product).quantity == 5

def test_product_price(first_product, second_product):
    assert first_product.price == 1700000
    assert second_product.price == 210000.0