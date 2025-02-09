import pytest


def test_category_init(first_category, second_category):
    assert first_category.name == "автомобили"
    assert (
        first_category.description
        == """Самодвижущееся транспортное средство с двигателем для перевозки грузов и пассажиров
         по безрельсовым путям"""
    )
    assert first_category.products_in_list == ["Hyundai i20", "Lada Vesta", "Daewoo Matiz"]
    assert len(first_category.products_in_list) == 3

    assert second_category.name == "стрелковое оружие"
    assert (
        second_category.description
        == """орудия (изделия), для стрельбы, изготовленные человеком для добычи зверя, развлечения (спорт),
         борьбы со своим противником или иного."""
    )
    assert len(second_category.products_in_list) == 3

    assert first_category.category_quantity == 2
    assert second_category.category_quantity == 2

    assert first_category.products_quantity == 6
    assert second_category.products_quantity == 6


def test_category_add_product(add_product_in_category):
    assert add_product_in_category.name == '55" QLED 4K'
    assert add_product_in_category.description == "Фоновая подсветка"
    assert add_product_in_category.price == 123000.0
    assert add_product_in_category.quantity == 7


def test_category_check_count_quantity(first_category, add_product_in_category):
    assert first_category.products_quantity == 9
    first_category.add_product(add_product_in_category)
    assert first_category.products_quantity == 10


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator) == 'Ружье служебное "Сайга-410СВ" калибра 410/76'
    assert next(product_iterator) == 'Ружье служебное многозарядное "Бекас-12М" калибра 12/70'
    assert next(product_iterator) == 'Карабин служебный самозарядный "Вепрь-12С Молот" (ВПО-205С) калибра 12/76'

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_middle_price(category_without_products):
    with pytest.raises(ZeroDivisionError):
        assert category_without_products.middle_price() == 0


def test_len_first_category(first_category):
    assert len(first_category.products_in_list) == 3

def test_len_second_category(second_category):
    assert len(second_category.products_in_list) == 3