from tests.conftest import first_category


def test_product_init(first_product):
    assert first_product.name == "hyundai i20"
    assert (
        first_product.description
        == """Cубкомпактный хетчбэк, выпускающийся с 2008 года. В большинстве стран Hyundai i20 пришёл
        на смену модели Getz"""
    )
    assert first_product.price == 1700000
    assert first_product.quantity == 5

def test_category_add_product(add_product_in_category):
    assert add_product_in_category.name == "55\" QLED 4K"
    assert add_product_in_category.description == "Фоновая подсветка"
    assert add_product_in_category.price == 123000.0
    assert add_product_in_category.quantity == 7
