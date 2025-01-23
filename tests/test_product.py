from src.product import Product
from tests.conftest import first_product


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


def test_product_price_setter(capsys, second_product):
    new_price = -100
    second_product.price = new_price
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    new_price = 800
    second_product.price = new_price
    assert second_product.price == 800


def test_product_str(first_product):
    assert str(first_product) == "hyundai i20, 1700000 руб. Остаток: 5 шт."


def test_add_products(fist_product_for_add, second_product_for_add):
    assert fist_product_for_add + second_product_for_add == 2541000
